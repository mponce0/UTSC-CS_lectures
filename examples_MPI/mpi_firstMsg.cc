#include <iostream>
#include <string>
#include <mpi.h>

using namespace std;

int main(int argc, char **argv) {
	int rank, size;
	int tag = 1;
	double msgsent, msgrcvd;
	MPI_Status rstatus;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	msgsent = 111.;
	msgrcvd = -999.;

	if (rank == 0) {
		MPI_Ssend(&msgsent, 1, MPI_DOUBLE, 1, tag, MPI_COMM_WORLD);
		cout << "Sent " + to_string(msgsent) + " from " + to_string(rank) + "\n";
	}

	if (rank == 1) {
		MPI_Recv(&msgrcvd, 1, MPI_DOUBLE, 0, tag, MPI_COMM_WORLD, &rstatus);
		cout << "Received " + to_string(msgrcvd) + " on " + to_string(rank) + "\n";
	}

	MPI_Finalize();
}
