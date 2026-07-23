# score.py
"""スコア計算および判定を行うモジュール"""

INITIAL_SCORE = 2000  # 初期スコア


def calculate_score(tries: int, elapsed_time: int = 0) -> int:
    """試行回数に応じて残りのスコアを計算する

    - 1〜4回目: 1回ごとに 100点 減点
    - 5回目以降 (ヒント表示後): 1回ごとに 200点 減点
    """
    score = INITIAL_SCORE

    for t in range(1, tries + 1):
        if t <= 4:
            score -= 100
        else:
            score -= 200

    #  時間による減点
    score -= elapsed_time  * 10       

    # スコアがマイナスにならないようにガード（必要に応じて）
    #return max(0, score)
    return score


def get_score_message(score: int) -> str:
    """残った点数に応じて評価メッセージを返す"""
    if score >= 1100:  # 1〜4回で正解
        return "素晴らしい！完璧な推測力ですね！"
    elif score >= 800:  # 5〜6回で正解
        return "ナイス！なかなか筋が良いですね。"
    elif score >= 400:  # 7〜8回で正解
        return "クリアおめでとう！粘り勝ちです。"
    else:  # 9〜10回で正解
        return "ギリギリセーフ！ヒヤヒヤしましたね。"