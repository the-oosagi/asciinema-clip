import sys
import json
from itertools import accumulate


class AsciinemaClipper:
    def __init__(
        self, input_filename: str, output_filename: str, cutoff: float
    ):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.cutoff = cutoff

    def execute(self):
        with open(self.input_filename) as f:
            txt = f.read().split("\n")

        timestamp = []
        rows = []
        for i, line in enumerate(txt):
            if line.strip():
                if line[0] == "[":
                    row = eval(line)
                    rows.append(row)
                    timestamp.append(row[0])

        time_diff = [
            time - timestamp[i - 1] if i > 0 else 0
            for (i, time) in enumerate(timestamp)
        ]

        time_diff_cut = []
        for time in time_diff:
            if (time > self.cutoff):
                val = self.cutoff
            else:
                val = time
            time_diff_cut.append(val)

        time_diff_cut = [0] + time_diff_cut[:-1]  # timestamp[0]

        timestamp_new = list(accumulate(time_diff_cut))
        for tsn, row in zip(timestamp_new, rows):
            row[0] = tsn

        out_str = ""
        for tsn, line in zip(timestamp_new, txt):
            if line.strip():
                if line[0] == "[":
                    comma_idx = line.index(",")
                    row = "[" + str(tsn) + (line[comma_idx:])
                elif line[0] == "{":
                    row = line
                else:
                    row = ""
                out_str += row + "\n"

        with open(self.output_filename, "w") as f:
            f.write(out_str)

