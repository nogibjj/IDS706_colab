import pandas as pd

df = pd.read_csv("NBA_2021.csv")


def test_best_efficient_player():
    df["Efficiency_Rating"] = (
        df["PTS"]
        + df["TRB"]
        + df["AST"]
        + df["STL"]
        + df["BLK"]
        - (df["FGA"] - df["FG"])
        - (df["FTA"] - df["FT"])
        - df["TOV"]
    )
    assert (
        df[df["G"] > 30][["Player", "Efficiency_Rating"]].nlargest(10, "Efficiency_Rating")[
            "Player"
        ][344]
        == "Nikola Jokić"
    )
    assert (
        df[df["G"] > 30][["Player", "Efficiency_Rating"]].nlargest(10, "Efficiency_Rating")[
            "Efficiency_Rating"
        ][344]
        ==  35.9
    )


def test_best_score_player():
    top_scorers_per_team = (
        (
            df[df["G"] > 20]
            .sort_values(["Tm", "PTS"], ascending=[True, False])
            .groupby("Tm")
            .head(1)
            .reset_index(drop=True)
        )
        .sort_values("PTS", ascending=False)
        .reset_index(drop=True)
    )
    assert top_scorers_per_team[["Tm", "Player", "PTS"]]["Player"][0] == "Stephen Curry"
    assert top_scorers_per_team[["Tm", "Player", "PTS"]]["PTS"][0] == 32.0
