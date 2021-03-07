// . . .
if ((rank % 2) == 0) {
	MPI_Ssend(&msgsent, 1, MPI_DOUBLE, right, tag, MPI_COMM_WORLD);
	MPI_Recv(&msgrcvd, 1, MPI_DOUBLE, left, tag, MPI_COMM_WORLD, &rstatus);
	// MPI_Sendrecv(&msgsent, 1, MPI_DOUBLE, right, tag,
	//		&msgrcvd, 1, MPI_DOUBLE, left, tag, MPI_COMM_WORLD, &rstatus);
} else {
	MPI_Recv(&msgrcvd, 1, MPI_DOUBLE, left, tag, MPI_COMM_WORLD, &rstatus);
	MPI_Ssend(&msgsent, 1, MPI_DOUBLE, right, tag, MPI_COMM_WORLD);
}
// . . .
 


$ mpirun -n 5 ./sendreceivePBC
  1: Sent 1.000000 and got 0.000000
  2: Sent 4.000000 and got 1.000000
  3: Sent 9.000000 and got 4.000000
  4: Sent 16.000000 and got 9.000000
  0: Sent 0.000000 and got 16.000000
