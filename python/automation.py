import pathlib as pth
import subprocess
from graph import Graph
import argparse
import csv


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("--executable", required=True, type=str, help="Executable path of binary for finding approx path")
    parser.add_argument("--resources", required=True, type=str, help="Directory that has graphs, vertex, approx sub-directories")

    return parser.parse_args()


def find_approx_vertex_cover(exec_path: pth.Path, graph_file: pth.Path, output_dir: pth.Path) -> None:
    args = [
        exec_path,
        graph_file,
        output_dir
    ]

    try: 
        process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as err:
        print("Unable to run the executable.", err, sep="\n")


def visualise_and_get_data(graph_file: pth.Path, vertex_cover_path: pth.Path, approx_path: pth.Path, output_dir: pth.Path) -> dict:
    g = Graph(graph_file, approx_path, vertex_cover_path, output_dir)
    g.save_visualisation()
    return g.get_data()


def main():
    opts = parse()

    res = pth.Path(opts.resources)
    executable = pth.Path(opts.executable)
    vertex_pth = res.joinpath("vertex")
    approx_dir = res.joinpath("approx")
    output_dir = res.joinpath("images")

    graphs = list(res.joinpath("graphs").glob("*.graph"))

    graphs = sorted(graphs)

    if not output_dir.exists():
        output_dir.mkdir()

    data_rows = []

    for files in graphs:
        find_approx_vertex_cover(executable, files, approx_dir)
        vertex_file = vertex_pth.joinpath(files.stem + ".vertex_cover")
        approx_file = approx_dir.joinpath(files.stem + ".maximal_matching")
        
        data = visualise_and_get_data(
            files,
            vertex_file, 
            approx_file, 
            output_dir
        )

        """
            "numNodes" : len(self.nodes),
            "numEdges" : len(self.edges),
            "sizeVertexCover" : len(self.vertex_cover),
            "sizeMaximalMatching" : len(self.matching_edges),
            "sizeApproxVertexCover" : len(self.approx_vertex_cover),
            "runtimeVertexCover" : self.brute_force_runtime,
            "runtimeApproxVertexCover" : self.approx_runtime
        """

        af = data['sizeApproxVertexCover'] / data['sizeVertexCover']

        data_r = [
            f"{data['numNodes']},{data['numEdges']}",
            f"{data['sizeVertexCover']}",
            f"{data['runtimeVertexCover'] * 10e-6:0.8f}",
            f"{data['sizeApproxVertexCover']}",
            f"{af:0.3f}",
            f"{data['runtimeApproxVertexCover'] * 10e-6:0.8f}"
        ]

        data_rows.append(data_r)

    header_row1 = ['(n, m)', 'P1', '', 'P2', '', '']
    header_row2 = ['', 'BF', '', 'AA', '', '']
    header_row3 = ['', 'Size', 'Time (in seconds)', 'Size', 'AF', 'Time (in seconds)']

    csv_file = res.joinpath("table_data.csv")

    with open(csv_file, 'w') as file:
        table = csv.writer(file)
        
        table.writerows([header_row1, header_row2, header_row3])
        
        table.writerows(data_rows)


if __name__ == "__main__":
    main()