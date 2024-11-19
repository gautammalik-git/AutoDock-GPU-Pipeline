import os
import glob
import concurrent.futures

def process_file(file_name):
    with open(file_name) as f:
        data = f.readlines()

    # Find line 1 and line 2
    line_1, line_2 = None, None
    for i, line in enumerate(data):
        if "Num" in line[34:40]:
            line_1 = i + 4
        elif "RMSD TABLE" in line:
            line_2 = i - 3
            break

    if line_1 is not None and line_2 is not None:
        relevant_lines = data[line_1:line_2]

        # Extract energy values and conformations
        energies = []
        for line in relevant_lines:
            try:
                conformations = int(line[36:40].strip())
                energy_value = line[10:16].strip()
                energies.append((conformations, energy_value))
            except ValueError:
                continue  # Skip lines with invalid numbers

        if energies:
            max_conformations, max_energy = max(energies, key=lambda x: x[0])
            final_energy = f"{os.path.basename(file_name)[:-4]} {max_energy} kcal/mol"
            return final_energy, max_conformations

    return None, None


def main():
    path = os.getcwd()
    file_path = f"{path}/*.dlg"
    file_names = sorted(glob.glob(file_path))  # Get and sort file names

    with open("Energy.txt", "w") as output:
        # Use ThreadPoolExecutor for parallel processing
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(process_file, file_names)

            # Write the results to the output file
            for final_energy, conformations in results:
                if final_energy:
                    print(final_energy)
                    print(f"Conformations: {conformations}\n")
                    output.write(f"{final_energy}\n")

if __name__ == "__main__":
    main()
