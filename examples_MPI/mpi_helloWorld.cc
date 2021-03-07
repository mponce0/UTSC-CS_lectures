#include <iostream>
#include <string>
#include <mpi.h>
using namespace std;

int main(int argc, char **argv) {

    int rank, size;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    cout << "Hello World, from task " +
	to_string(rank) + " of " +
	to_string(size) + " \n";

    MPI_Finalize();
}
