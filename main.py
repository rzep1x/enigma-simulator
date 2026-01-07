import argparse
from gui import guiMain
import sys
from enigma import Enigma, MalformedDataError, InvalidComponentError
from components import Rotor, Plugboard, Reflector


def run_batch_mode(input_data, is_file, output_file, settings_file):
    print("------BATCH MODE------")
    print(f"Settings: {settings_file}")

    placeholder_rotor = Rotor("I", 0, 0)
    placeholder_plugboard = Plugboard("")
    placeholder_reflector = Reflector("B")
    enigma = Enigma(
        placeholder_rotor, placeholder_rotor,
        placeholder_rotor, placeholder_reflector,
        placeholder_plugboard
    )
    try:
        with open(settings_file, 'r') as file_handle:
            enigma.load_enigma_settings(file_handle)
    except IsADirectoryError:
        print(f"ERROR: Settings file is a directory: '{settings_file}'")
        return
    except FileNotFoundError:
        print(f"ERROR: Settings file not found: '{settings_file}'")
        return
    except PermissionError:
        print(f"ERROR: No permission to read settings file: '{settings_file}'")
        return
    except (MalformedDataError, InvalidComponentError) as e:
        print(f"Settings error: {e}")
        return

    content = ""
    if is_file:
        print(f"Input file: {input_data}")
        try:
            with open(input_data, 'r') as file_handle:
                content = file_handle.read()
        except FileNotFoundError:
            print(f"ERROR: Input file not found: '{input_data}'")
            return
        except IsADirectoryError:
            print(f"ERROR: Input file is a directory: '{input_data}'")
            return
        except PermissionError:
            print(f"ERROR: No permission to read input file: '{input_data}")
            return
    else:
        content = input_data
        print(f"Input: {content}")

    result = enigma.encrypt(content)
    print(f"Encrypted text: {result}")

    try:
        with open(output_file, 'w') as file_handle:
            file_handle.write(result)
        print(f"Success: encrypted text saved to {output_file}")
    except IsADirectoryError:
        print(f"ERROR: Output file is a directory: '{output_file}'")
        return
    except PermissionError:
        print(f"ERROR: No permission to read output file: '{output_file}")
        return
    except OSError as e:
        print(f"ERROR: Could not write to output file: {e}")
        return


def main():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', "--input", help="File path to input file")
    group.add_argument("-t", "--text", help="Text to cipher")

    parser.add_argument("-o", "--output", help="File path to output file")
    parser.add_argument("-s", "--settings", help="File path to json file with settings of enigma")

    args = parser.parse_args()

    has_input = args.input or args.text
    has_output = args.output
    has_settings = args.settings

    if has_input and has_output and has_settings:
        is_file = True if args.input else False
        input = args.input if is_file else args.text
        run_batch_mode(input, is_file, args.output, args.settings)

    elif has_input or has_output or has_settings:
        print("Error: Batch mode requires 3 arguments: input(-i or -t), output(-o) and settings(-s)")

    else:
        guiMain(sys.argv)


if __name__ == "__main__":
    main()
