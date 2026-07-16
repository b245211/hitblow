"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=3):

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====

    from .duplicate import ask_duplicate

    allow_duplicate = ask_duplicate()
    secret = make_secret(digits, allow_duplicate)

    max_tries = 10
    print(f"10回以内にあててね")

    tries = 0
    while True:

        if tries >= max_tries:
            print(f"残念！ゲームオーバー…（答えは {secret} でした）")
            break
            
        remaining = max_tries - tries
        print(f"--- [残り {remaining} 回] ---")
        
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")

        if tries == 5:
            odd = sum(int(d) % 2 == 1 for d in secret)
            even = digits - odd
            print("=== ヒント ===")
            print(f"答えには奇数が {odd} 個、偶数が {even} 個含まれています。")


        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break
