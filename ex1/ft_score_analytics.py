import sys


def main() -> None:
    args = sys.argv[1:]
    score_list = []
    print("=== Player Score Analytics ===")
    if not args:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")
        return
    for arg in args:
        try:
            int_arg = int(arg)
            score_list.append(int_arg)
        except ValueError:
            print(f"Error: '{arg}' is not a valid score (must be a number)")
            return
    print(f"Scores processed: {score_list}")
    print(f"Total players: {len(score_list)}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list) / len(score_list)}")
    print(f"High score: {max(score_list)}")
    print(f"Low score: {min(score_list)}")
    print(f"Score range: {max(score_list) - min(score_list)}")


main()
