import re

class ScorecardParser:

    def __init__(self):
        self.pattern = r"([A-Za-z ]+)\s+(\d+)\((\d+)\)"

    def read_file(self, filename, team):

            try:

                with open(filename, "r") as file:

                    # Clear existing players before loading
                    team.get_players().clear()

                    for line in file:

                        line = line.strip()

                        # Skip empty lines
                        if not line:
                            continue


                        match = re.fullmatch(
                            self.pattern,
                            line
                        )


                        if match:

                            name = match.group(1).strip()
                            runs = int(match.group(2))
                            balls = int(match.group(3))


                            player = Batsman(
                                name,
                                runs,
                                balls
                            )


                            team.add_player(player)


                        else:

                            print(
                                f"Invalid record skipped: {line}"
                            )


                print("\nScorecard loaded successfully!")


            except FileNotFoundError:

                print("\nFile not found!")


            except Exception as e:

                print(
                    f"\nError occurred: {e}"
                )

    # -----------------------------
    # Load Scorecard
    # -----------------------------
    def load_file(self, filename, team):

        try:

            with open(filename, "r") as file:

                # Clear old data
                team.get_players().clear()

                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    match = re.fullmatch(self.pattern, line)

                    if match:

                        name = match.group(1).strip()
                        runs = int(match.group(2))
                        balls = int(match.group(3))

                        player = Batsman(name, runs, balls)

                        team.add_player(player)

                    else:

                        print(f"Invalid record skipped: {line}")

            print("\nScorecard loaded successfully!")

        except FileNotFoundError:

            print("\nFile not found!")

        except Exception as e:

            print(f"\nError: {e}")

    # -----------------------------
    # Save Scorecard
    # -----------------------------
    def save_file(self, filename, team):

        try:

            with open(filename, "w") as file:

                for player in team.get_players():

                    file.write(
                        f"{player.get_name()} "
                        f"{player.get_runs()}({player.get_balls()})\n"
                    )

            print("\nScorecard saved successfully!")

        except Exception as e:

            print(f"\nError: {e}")