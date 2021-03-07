#include <mpi.h>
#include <omp.h>
#include <iostream>

int main(int argc, char ** argv) {

	int size,rank;

	MPI_Init(&argc,&argv);
	MPI_Comm_get_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_get_size(MPI_COMM_WORLD,&size);

	#pragma omp parallel for
	for (int i=0;i<4;i++)
		std::cout << "Hello world from thread "
			<< omp_get_thread_num() << std::endl;

	MPI_Finalize();
}
