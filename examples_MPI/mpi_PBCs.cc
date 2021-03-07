#include <iostream>
#include <string>
#include <mpi.h>

using namespace std;

int main(int argc, char **argv) {
	int rank, size, left, right, tag = 1; 
	double msgsent, msgrcvd;
	MPI_Status rstatus;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	left = rank - 1;
	//if (left < 0) left = MPI_PROC_NULL;
	if (left < 0) left = size-1; // Periodic BC

	right = rank + 1;
	// if (right >= size) right = MPI_PROC_NULL;
	if (right >= size) right = 0; // Periodic BC

	// messages
	msgsent = rank*rank;
	msgrcvd = -999.;

	// communication
	//MPI_Ssend(&msgsent, 1, MPI_DOUBLE, right, tag, MPI_COMM_WORLD);
	//MPI_Recv(&msgrcvd, 1, MPI_DOUBLE, left, tag, MPI_COMM_WORLD, &rstatus);
	if ((rank % 2) == 0) {
		MPI_Ssend(&msgsent, 1, MPI_DOUBLE, right, tag, MPI_COMM_WORLD);
		MPI_Recv(&msgrcvd, 1, MPI_DOUBLE, left, tag, MPI_COMM_WORLD, &rstatus);
		// MPI_Sendrecv(&msgsent, 1, MPI_DOUBLE, right, tag,
        
		//              &msgrcvd, 1, MPI_DOUBLE, left, tag, MPI_COMM_WORLD, &rstatus);
	} else {
		MPI_Recv(&msgrcvd, 1, MPI_DOUBLE, left, tag, MPI_COMM_WORLD, &rstatus);
		MPI_Ssend(&msgsent, 1, MPI_DOUBLE, right, tag, MPI_COMM_WORLD);
	}

	cout << to_string(rank) + ": Sent " + to_string(msgsent)
		+ " and got " + to_string(msgrcvd) + "\n";

	MPI_Finalize();
}
