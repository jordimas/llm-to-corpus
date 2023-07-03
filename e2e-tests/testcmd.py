import unittest
import os
import tempfile


class TestCmd(unittest.TestCase):
    def test_help_runs(self):
        cmd = "llm-to-corpus --help> /dev/null"
        exit_code = os.system(cmd)
        self.assertEqual(0, exit_code)

    def test_models_runs(self):
        cmd = "llm-to-corpus --models> /dev/null"
        exit_code = os.system(cmd)
        self.assertEqual(0, exit_code)

    def _test_model_boom(self):
        full_path = os.path.realpath(__file__)
        path, filename = os.path.split(full_path)
        input_file = os.path.join(path, "english.txt")

        with tempfile.TemporaryDirectory() as directory:
            output_file = os.path.join(directory, "output.txt")
            isExist = os.path.exists(directory)
            print(f"directory: {isExist}")
            cmd = f'llm-to-corpus {input_file} {output_file} "Translate the following text to Catalan:" --model mt0-xxl-mt'
            print(cmd)
            exit_code = os.system(cmd)
            self.assertEqual(0, exit_code)

            with open(output_file, "r") as fh_r:
                content = fh_r.readlines()

        self.assertEqual(1, len(content))
        self.assertEqual(
            "Quantes persones hi haurà a la festa demà?", content[0].rstrip()
        )


if __name__ == "__main__":
    unittest.main()
