class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if path=='':
            return True
        if cols<=0 or rows<=0:
            return False
        matrix=[matrix[r*cols:(r+1)*cols] for r in range(rows)]
        arrive=[[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==path[0]:
                    if self.ishasPath1(matrix,rows,cols,i,j,path[1:],arrive):
                        return True
        return False

    def ishasPath(self,matrix,rows,cols,i,j,path,arrive):
        if path=='':
            return True
        isPath=False
        print (path,i,j)
        arrive[i][j]=1 #一条路径不能同时经过一个格子两次
        if i>0 and arrive[i-1][j] != 1 and matrix[i-1][j]==path[0]:
            isPath |= self.ishasPath(matrix,rows,cols,i-1,j,path[1:],arrive)
        if j>0 and arrive[i][j-1] != 1 and matrix[i][j-1]==path[0]:
            isPath |= self.ishasPath(matrix,rows,cols,i,j-1,path[1:],arrive)
        if i<rows-1 and arrive[i+1][j] != 1 and matrix[i+1][j]==path[0]:
            isPath |= self.ishasPath(matrix,rows,cols,i+1,j,path[1:],arrive)
        if j<cols-1 and arrive[i][j+1] != 1 and matrix[i][j+1]==path[0]:
            isPath |= self.ishasPath(matrix,rows,cols,i,j+1,path[1:],arrive)
        arrive[i][j]=0
        return isPath

    def ishasPath1(self,matrix,rows,cols,i,j,path,arrive):
        if path=='':
            return True
        print (path,i,j)
        arrive[i][j]=1 #一条路径不能同时经过一个格子两次
        if i>0 and arrive[i-1][j] != 1 and matrix[i-1][j]==path[0]:
            return self.ishasPath(matrix,rows,cols,i-1,j,path[1:],arrive)
        if j>0 and arrive[i][j-1] != 1 and matrix[i][j-1]==path[0]:
            return self.ishasPath(matrix,rows,cols,i,j-1,path[1:],arrive)
        if i<rows-1 and arrive[i+1][j] != 1 and matrix[i+1][j]==path[0]:
            return self.ishasPath(matrix,rows,cols,i+1,j,path[1:],arrive)
        if j<cols-1 and arrive[i][j+1] != 1 and matrix[i][j+1]==path[0]:
            return self.ishasPath(matrix,rows,cols,i,j+1,path[1:],arrive)
        arrive[i][j]=0
        return False

if __name__=='__main__':
    solve=Solution()
    matrix="ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS"
    rows=5
    cols=8
    path="SGGFIECVAASABCEHJIGQEM"
    print (solve.hasPath(matrix,rows,cols,path))