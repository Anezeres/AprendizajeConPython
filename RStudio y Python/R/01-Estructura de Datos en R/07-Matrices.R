#Matrices

#como definirlas
#matrix(vector,nrow = n,byrow = valor_logico)

#nrow = numero de filas

#byrow = TRUE o FALSE, 
#ncol = En lugar de byrow

M = matrix(1:12,nrow = 4)
M

M = matrix(1:12,nrow = 4,byrow = TRUE)
M

M = matrix(1:12,nrow = 3)
M

M = matrix(1:12,nrow = 5) #R me da un quieto
M




M = matrix(1,nrow = 4,ncol = 6)
M


#Como construir matrices
#rbind()
#cbind()

M
rbind(M,c(1,2,3),c(-1,-2,-3))
rbind(c(1,2,3),c(-1,-2,-3))
cbind(c(1,2,3),c(-1,-2,-3))

diag(c(1,2,3,4))#Matriz diagonal a partir de un vector
diag(5,nrow = 5)
diag(5,nrow = 3)

#Submatrices 
# matriz[i,j]
# matriz[i,]
# matriz[,j]



#Funciones
#diag(M)
#nrow(M)
#ncol(M)
#dim(M)
#sum(M)
#prod(M)
#mean(M)
#rowSums(M)
#colSums(M)
#colMean(M)
#rowMean(M)









