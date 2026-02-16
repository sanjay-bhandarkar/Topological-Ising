character(len=20) function str(Int)
implicit none
integer,intent(in) :: Int
character(len=20) :: temp
write(temp,'(I10)')Int
write(str,'(A20)')adjustl(temp)
end function str

program Analysis
    implicit none
    integer,parameter :: n_part = 400, n_snapshots = 20001,n_skip = 9, n_files = 40,arr_size = n_part
    integer,parameter :: data_size = n_files*n_part*n_snapshots/100
    integer :: i,j,k,a(arr_size),p,m
    real :: b(arr_size),c(arr_size),d(arr_size),e(arr_size),f(arr_size),g(arr_size),h(arr_size)
    real :: big_loop1(data_size), big_loop2(data_size)
    real :: small_loop1(data_size), small_loop2(data_size)
    character(len=20) :: str

    p = 0
    big_loop1 = 0.0
    big_loop2 = 0.0
    small_loop1 = 0.0
    small_loop2 = 0.0

    open(171, file = '/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Plots/BL1.dat', action = 'write', position = 'append')
    open(172, file = '/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Plots/BL2.dat', action = 'write', position = 'append')
    open(173, file = '/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Plots/SL1.dat', action = 'write', position = 'append')
    open(174, file = '/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Plots/SL2.dat', action = 'write', position = 'append')
    ! open(171, file = '/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent27/Plots/mon1.dat', &
    ! action = 'write', position = 'append')
    ! open(172, file = '/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent27/Plots/mon2.dat', &
    ! action = 'write', position = 'append')



    do p = 1,n_files

        open(70+p, file = '/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Exp'//trim(str(p))//'/Positions.dat')

        ! if (p == 3) cycle

        print*, p

        do i = 1,n_snapshots

            if (mod(i,1)==0) then 

            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0

            do j = 1,n_skip
                read(70+p,*)
            end do

            do k = 1,n_part
                read(70+p,*) a(k), b(k), c(k), d(k), e(k), f(k), g(k), h(k)
            end do

            do m = 1, n_part
                if (b(m)==1) write(173,*) e(m)
                if (b(m)==2) write(171,*) e(m)
                if (b(m)==3) write(174,*) e(m)
                if (b(m)==4) write(172,*) e(m) 
            end do 

            ! do m = 1, n_part
            !     if (b(m)==2) then 
            !         big_loop1((p-1)*n_snapshots*n_part + (i-1)*n_part + a(m)) = e(m)
            !     end if

            !     if (b(m)==4) then 
            !         big_loop2((p-1)*n_snapshots*n_part + (i-1)*n_part + a(m)) = e(m)
            !     end if

            !     if (b(m)==1) then 
            !         small_loop1((p-1)*n_snapshots*n_part + (i-1)*n_part + a(m)) = e(m)
            !     end if

            !     if (b(m)==3) then 
            !         small_loop2((p-1)*n_snapshots*n_part + (i-1)*n_part + a(m)) = e(m)
            !     end if
            ! end do 

            end if

        end do
    
        close(70+p)

    end do 


    ! do i = 1, data_size
    !     write(171,*) big_loop1(i)
    ! end do 

    ! do i = 1, data_size
    !     write(172,*) big_loop2(i)
    ! end do

    ! do i = 1, data_size
    !     write(173,*) small_loop1(i)
    ! end do

    ! do i = 1, data_size
    !     write(174,*) small_loop2(i)
    ! end do

end program Analysis