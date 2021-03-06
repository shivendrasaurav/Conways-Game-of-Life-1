#CONWAY's GAME OF LIFE
#AUTHOR : github.com/outcastdreamer (SAKET SAVARN)

		#1)*Nvar_init_M -> The initial starting cordinate on X-Axis. It's static & -ve in nature (Doesn't change).
		#2)*Nvar_init_N -> The initial starting cordinate on Y-Axis. It's static & +ve in nature (Doesn't change).
			    ############# NOTE -> BOTH *init_M & *init_N should be equal in magnitude and opposite in sign.
		#3)*Nvar_M      -> It is not static in nature and variates from *Init_M to -*Init_M (EG: -1 to 1)
		#4)*Nvar_N 	    -> It is not static in nature and variates from *Init_N to -*Init_N (EG: 1 to -1)
		#5)*Nvar_final_M-> It is the last value of *Init_M, i.e if *Init_M = -1, then *final_M = 1.
		#6)*Nvar_final_N-> It is the last value of *Init_N, i.e if *Init_N = 1, then *final_N = -1.


		#7)*Nvar_init_J -> The VIRTUAL starting cordinate on X-Axis which is equal to (*init_M - 1) in magnitude.
		#8)*Nvar_init_K -> The VIRTUAL starting cordinate on Y-Axis which is equal to (*init_N + 1) in magnitude.
				############# NOTE -> EG: if *init_M & *init_N is equal to (-1,1), then *init_J and
						 ####         *init_k = (-1-1,1+1) = (-2,2). They are not the real starting cordinates
						 ####		  but only serve to check neighbours for cells like (-1,1), (0,1), etc.
		#9)*Nvar_J       -> Variates from *Init_J to -*Init_J or *Final_J.
		#10)*Nvar_K      -> Variates from *Init_K to -*Init_K or *Final_K.
		#11)*Nvar_final_J-> Equivalent to -ve of *Init_J, i.e -*Init_J. (EG: if *Init_J=-2, then *Final_J=2).
		#12)*Nvar_final_K-> Equivalent to -ve of *Init_K, i.e -*Init_K. (EG: if *Init_K=2, then *Final_K=-2).


		#13)*List_real_rowkeys    -> Consists of actual number of rows for cordinates (m,n).
								     #EG: *real_rowkeys=['r1','r2','r3'] for (m,n)=(-1,1)
		#14)*List_virtual_rowkeys -> Consists of 2 extra rows from the actual rows to represent,ie (j,k) no. of rows.
								     #EG: *virtual_rowkeys=['r1,'r2','r3','r4','r5'] for (m,n)=(-1,1) and (j,k)=(-2,2)
								     #Here, 'r1' and 'r5' elems are virtual in nature & represent elems -> [-2,2],[-1,2],etc.
		#15)*List_real_elems      -> Shows all the real cordinates. (EG: for (m,n)=(-1,1), *real_elems=
								     #[[-1,1],[0,1],[1,1],[-1,0],[0,0],[1,0],[-1,-1],[0,-1],[1,-1]]))
		#16)*List_virtual_elems   -> Shows all the virtual cordinates. (EG: for (j,k)=(-2,2), i.e. (m,n)=(-1,1)
								     #*virtual_elems =
								     #[-2,2],[-1,2],[0,2],[1,2],[2,2],
								     #[-2,1],[-1,1],[0,1],[1,1],[2,1],
								     #[-2,0],[-1,0],[0,0],[1,0],[2,0],
								     #[-2,-1],[-1,-1],[0,-1],[1,-1],[2,-1]
								     #[-2,-2],[-1,-2],[0,-2],[1,-2],[2,-2])


		#17)*List_real_row_elems_count    -> Consists of number of elements in a row for (m,n), EG: for (-1,1)
										     #real_row_elems_count = ['■','■','■'] for [[-1,1],[0,1],[1,1]]
										     #It only represents one row, not all rows. <Only X-axis changes>
		#18)*List_virtual_row_elems_count -> Consists of virtual number of elements in a row for (j,k),
										     #EG: for (-2,2) (here, (m,n)=(-1,1))
										     #virtual_row_elems_count = ['■','■','■','■','■'] for
										     #[[-2,2],[-1,2],[0,2],[1,2],[-2,2]]   <Only X-axis changes>
										     #It only represents one row, not all rows.

		#19)*List_real_column_elems_count    -> Consists of number of elements in a column for (m,n)
											    #EG: for (-1,1) real_column_elems_count =
											    #['■','■','■'] for [[-1,1],[-1,0],[-1,-1]] <Only Y-axis changes>
										        #It only represents one column, not all columns.
		#20)*List_virtual_column_elems_count -> Consists of virtual number of elements in a column for (j,k),
										        #EG: for (-2,2) (here, (m,n)=(-1,1))
										        #virtual_column_elems_count = ['■','■','■','■','■'] for
										        #[[-2,2],[-2,1],[-2,0],[-2,-1],[-2,-2]] <Only Y-axis changes>
										        #It only represents one column, not all columns.

		#21)*Var_occpd    -> Stands for -occupied-, and has value "■".
		#22)*Var_empty    -> Stands for -empty-, and has value "□".


		#23)*Dict_VIRTUAL_ROWKEYS_ELEMS  -> It consists of rowkeys as INITIAL KEYS i.e. 'r1','r2'...,etc
											#which also consist of virtual rows (therefore,it's related to
											#*List_virtual_rowkeys). These rowkeys 'r1', etc.. consist of
											#cordinates of that row (row 'r1' & 'r5' are completely virtual
											#as they have [-2,2] and [-2,-2] as elements which are not real in nature)
											#The values of rowkeys is a list where each element in the list is a
											#dictionary consisting of cordinates as a key. If the cordinate is
											#virtual in nature (EG: [-2,2]) then it's value is 0 if not then it's
											#value maybe "□" or "■". Example on Line 204

		#24)*List_REAL_ELEMS_KEYS        -> It's a 2D list which has REAL cordinates as elements.
											#EG: [[-1,1],[0,1],[1,1],[-1,0],[0,0],[1,0],[-1,-1],[0,-1],[1,-1]]
		#25)*List_ULTIMATO_COMBO_ELEMS   -> It a 2D List where there are 9 elements in the sub-list with the
											#4th index or 5th element been the center cordinate for checking
											#it's eight neighbouring cells/elements which may be real or virtual.
											#Each element in the sub-list is actually a dictinary which has
											#value 0 if the key is a virtual cordinate and the value is
											#"□" or "■" if the key is real and existing.
											#EG: For (m,n) = (-1,1) List_ULTIMATO_COMBO_ELEMS ->
											#[
											#  [
											#   {'[-2,2]':0},{'[-1,2]':0},{'[0,2]':0},
											#   {'[-2,1]':0},{'[-1,1]':'□'},{'[0,1]':'■'}, Here, center=[-1,1]
											#   {'[-2,0]':0},{'[-1,0]':'■'},{'[0,0]':'■'}                (m,n)
											#  ],
											#  [
											#   {'[-1,2]':0},{'[0,2]':0},{'[1,2]':0},
											#   {'[-1,1]':'□'},{'[0,1]':'■'},{'[1,1]':'□'}, Here, center=[0,1]
											#   {'[-1,0]':'■'},{'[0,0]':'■'},{'[1,0]':'□'}
											#  ]
											#  .
											#  .
											#  .
											#  [
											#   {'[0,0]':'■'},{'[1,0]':'□'},{'[2,0]':0},
											#   {'[0,-1]':'□'},{'[1,-1]':'□'},{'[2,-1]':0} Here, center=[1,-1]
											#   {'[0,-2]':0},{'[1,-2]':0},{'[2,-2]':0}				    (-m,-n)
											#  ]
											#]
											#Total Count -> No. of boxes x 9 => here, 9x9 = 81 elements.

		#26)*List_all        -> #Consists of dictionaries as elements in the list where the key to each dictionary is
						        #a virtual or real cordinate whose value maybe 0 or maybe "□" or "■".
		#27)*List_all_real   -> #Consists of dictionaries as elements in the list where the key to each dictionary is
						        #a real cordinate whose value maybe "□" or "■".
						        #EG: [{'[-1, 1]':"□"},{'[0, 1]':"□"}....] for (m,n)=(-1,1)


		#28)*Nvar_game_instance  -> Starts from 0 and increases by 1 everytime a new instance or generation
									#in the game occurs. It's used to keep in check the number of moves taken
									#by the game.




import os
from pprint import pprint as pprint
from time import sleep as sl
from sys import platform
import random as ran

class Game_Of_Life:
#INITIALIZATION
	def __init__(self,
					Nvar_init_M=-1, Nvar_M=-1, Nvar_final_M=1, Nvar_init_N=1, Nvar_N=1, Nvar_final_N=-1,
					Nvar_init_J=-2, Nvar_J=-2, Nvar_final_J=2, Nvar_init_K=2, Nvar_K=2, Nvar_final_K=-2,
					List_real_rowkeys=[], List_virtual_rowkeys=[],
					List_real_elems=[], List_virtual_elems=[],
					List_real_row_elems_count=[], List_virtual_row_elems_count=[],
					List_real_column_elems_count=[], List_virtual_column_elems_count=[],
					Var_occpd="\u25A0",Var_empty="\u25A1",
					Dict_VIRTUAL_ROWKEYS_ELEMS={},
					List_REAL_ELEMS_KEYS=[],
					List_ULTIMATO_COMBO_ELEMS=[],
					List_all=[],List_all_real=[],
					Nvar_game_instance=0
				):
		self.Nvar_init_M=Nvar_init_M
		self.Nvar_M=Nvar_M
		self.Nvar_final_M=Nvar_final_M
		self.Nvar_init_N=Nvar_init_N
		self.Nvar_N=Nvar_N
		self.Nvar_final_N=Nvar_final_N
		self.Nvar_init_J=Nvar_init_J
		self.Nvar_J=Nvar_J
		self.Nvar_final_J=Nvar_final_J
		self.Nvar_init_K=Nvar_init_K
		self.Nvar_K=Nvar_K
		self.Nvar_final_K=Nvar_final_K
		self.List_real_rowkeys=List_real_rowkeys
		self.List_virtual_rowkeys=List_virtual_rowkeys
		self.List_real_elems=List_real_elems
		self.List_virtual_elems=List_virtual_elems
		self.List_real_row_elems_count=List_real_row_elems_count
		self.List_virtual_row_elems_count=List_virtual_row_elems_count
		self.List_real_column_elems_count=List_real_column_elems_count
		self.List_virtual_column_elems_count=List_virtual_column_elems_count
		self.Var_occpd="\u25A0"
		self.Var_empty="\u25A1"
		self.Dict_VIRTUAL_ROWKEYS_ELEMS=Dict_VIRTUAL_ROWKEYS_ELEMS
		self.List_REAL_ELEMS_KEYS=List_REAL_ELEMS_KEYS
		self.List_ULTIMATO_COMBO_ELEMS=List_ULTIMATO_COMBO_ELEMS
		self.List_all=List_all
		self.List_all_real=List_all_real
		self.Nvar_game_instance=0
		self.Grid()
#GRID DEVELOPMENT WITH VIRTUAL ELEMS ENVIRONMENT TOO.
	def Grid(self):
		if platform=="linux" or platform=="linux2":
			os.system("clear")
		elif platform=="win32":
			os.system('cls')
		print ("\t\t\t\t\t\t\t\t\t~ WELCOME TO THE GAME OF LIFE ~")
		print ("\n\n   Kindly note that the values for X and Y coordinates must be equal in magnitude and opposite in sign where X cordinate has -ve value and Y cordinate has +ve value!!")
		print ("\n\n\tThe values \"-10\" for X cooridnate and \"10\" for Y cooridnate are tested to be the best performance wise and hence I suggest you to use those values!")
		self.Nvar_init_M=1
		self.Nvar_init_N=-2
		while abs(self.Nvar_init_M)!=abs(self.Nvar_init_N):
			while self.Nvar_init_M>=0:
				try:
					self.Nvar_init_M=int(input("\n\n\t\tEnter value for X cordinate (Kindly enter -ve value only) : "))
				except ValueError:
					print ("\n\t\t\tError! You entered wrong value(s). Kindly try again! ")
					self.Nvar_init_M=1
			while self.Nvar_init_N<=0:
				try:
					self.Nvar_init_N=int(input("\t\tEnter value for Y cordinate (Kindly enter +ve value only) : "))
				except ValueError:
					print ("\n\t\t\tError! You entered wrong value(s). Kindly try again! ")
					self.Nvar_init_N=-2
			if abs(self.Nvar_init_M)!=abs(self.Nvar_init_N):
				print ("\n\tERROR!! Magnitude of X co-odinate is not equal to Y cordinate, i.e, their sign may be different \n\tbut absolute value must be same. Please try again!")
				self.Nvar_init_M=1
				self.Nvar_init_N=-2
			else:
				pass
		self.Nvar_M , self.Nvar_N = self.Nvar_init_M , self.Nvar_init_N
		self.Nvar_final_M , self.Nvar_final_N = - self.Nvar_init_M, - self.Nvar_init_N
		############################################
		self.Nvar_init_J , self.Nvar_init_K = self.Nvar_init_M - 1, self.Nvar_init_N + 1
		self.Nvar_J , self.Nvar_K = self.Nvar_init_J , self.Nvar_init_K
		self.Nvar_final_J , self.Nvar_final_K = - self.Nvar_init_J, - self.Nvar_init_K
		############################################
		self.List_real_row_elems_count=[]
		self.List_real_column_elems_count=[]
		self.List_real_elems=[]
		self.Nvar_M=self.Nvar_init_M
		self.Nvar_N=self.Nvar_init_N
		while self.Nvar_N!=self.Nvar_final_N-1:     #if Nvar_N = 1, then final_N-1 = - 1 - 1 = -2,
													#coz we want loop to break at -1.
													#This sets number of columns.
													###########################################
			while self.Nvar_M!=self.Nvar_final_M+1:	#if Nvar_M = -1, then final_M+1 = 1 + 1 = 2,
													#coz we want to break the loop at 1 itself.
													#This sets number of rows.
				self.List_real_elems+=[[self.Nvar_M , self.Nvar_N],]
				self.Nvar_M+=1
			self.Nvar_N-=1
			self.Nvar_M=self.Nvar_init_M
			self.List_real_row_elems_count+=[self.Var_occpd,]
			self.List_real_column_elems_count+=[self.Var_occpd,]
		"""pprint(self.List_real_row_elems_count)
		print ("\n\n")
		pprint(self.List_real_column_elems_count)
		print ("\n\n")
		pprint(self.List_real_elems)"""
		##########################################################################################
		while self.Nvar_K!=self.Nvar_final_K-1:     #if Nvar_K = 2, then final_K-1 = - 2 - 1 = -3,
													#coz we want loop to break at -2.
													#This sets number of columns.
													##############################################
			while self.Nvar_J!=self.Nvar_final_J+1:	#if Nvar_M = -1, then final_M+1 = 2 + 1 = 3,
													#coz we want to break the loop at 2 itself.
													#This sets number of rows.
				self.List_virtual_elems+=[[self.Nvar_J, self.Nvar_K],]
				self.Nvar_J+=1
			self.Nvar_K-=1
			self.Nvar_J=self.Nvar_init_J
			self.List_virtual_row_elems_count+=[self.Var_occpd,]
			self.List_virtual_column_elems_count+=[self.Var_occpd,]
		"""pprint(self.List_virtual_row_elems_count)
		print ("\n\n")
		pprint(self.List_virtual_column_elems_count)
		print ("\n\n")
		pprint(self.List_virtual_elems)"""
		##########################################################################################
		self.List_real_rowkeys=['r%d'%(i+1) for i in range(len(self.List_real_row_elems_count))]
		self.List_virtual_rowkeys=['r%d'%(i+1) for i in range(len(self.List_virtual_row_elems_count))]
		#pprint (self.List_real_rowkeys)
		#pprint (self.List_virtual_rowkeys)
#################################################################################################################
#################################################################################################################
#CREATING THE ULTIMATE DICTIONARY CONTAINING ALL THE VIRTUAL & REAL ELEMENTS i.e. ONE CONTAINING ALL VIRTUAL ROWS
#EG: Dict_VIRTUAL_ROWKEYS_ELEMS={'r1':[{'[-2,2]':0},{'[-1,2]':0},..........{'[1,2]':0},{'[2,2]':0}],
								#'r2':[{'[-2,1]':0},{'[-1,1]':'□'}..........{'[1,1]':'□'},{'[2,1]':'0'}],
								#'r3':[{'[-2,0]':0},{'[-1,0]':'□'}..........{'[1,0]':'□'},{'[2,0]':'0'}],
								#'r4':[{'[-2,-1]':0},{'[-1,-1]':'□'}..........{'[1,-1]':'□'},{'[2,-1]':'0'}],
								#'r5':[{'[-2,-2]':0},{'[-1,-2]':'□'}..........{'[1,-2]':'□'},{'[2,-2]':'0'}],
								#}
#This is an example for (m,n)=(-1,1) and (j,k)=(-2,2). All keys having X or Y cordinates as -2 or 2 have
#0 as their value as they are virtual or imaginary and don't really exist in reality in the game display.
#################################################################################################################
#################################################################################################################
		self.Dict_VIRTUAL_ROWKEYS_ELEMS={}
		dict_temp={} ; list_temp=[]
		j=0 ; k=0
		self.Nvar_J=self.Nvar_init_J ; self.Nvar_K=self.Nvar_init_K
		while (k!=len(self.List_virtual_column_elems_count)):
			while (j!=len(self.List_virtual_row_elems_count)):
				list_temp.append({str([self.Nvar_J , self.Nvar_K]):0})
				self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[k]] = list_temp
				j+=1
				self.Nvar_J+=1
			list_temp=[]
			j=0
			self.Nvar_J=self.Nvar_init_J
			k+=1
			self.Nvar_K-=1
		self.The_choice()
		#pprint (self.Dict_VIRTUAL_ROWKEYS_ELEMS)
#FUTURE NOTE -> Make Birth & Death as seperate user-defined function in the future and make another
				#user-defined function named decide or logic which decides wheter a cell will die, birth or
				#remain stable. As in case a scenario arises where if birth and death interfere this func. will
				#decide the best route. Rememeber the Conway's rule properly and then see if this future note
				#is valid in pointing out that interference b/w death and birth is possible or not.
#################################################################################################################
#################################################################################################################
###SETTING UP ALREADY SELECTED OR ALIVE OR INITIAL CELLS/ELEMS (TO START THE ZERO-PERSON GAME) AND DISTINGUISHING
###BETWEEN VIRTUAL ELEMS BY PUTTING THEIR VALUES AS 0 (defualt value) REAL ELEMS VALUES AS "□" AND MANUALLY
###SELECTED ONE AS "■" in Dict_VIRTUAL_ROWKEYS_ELEMS. THIS IS THE BASE OF THE GAME TO WORK.#######################
#################################################################################################################
#################################################################################################################
		#GLIDER => List_selected_elems=['[-9, 10]','[-8, 9]','[-10, 8]','[-9, 8]','[-8, 8]']
		"""WEIRD S => List_selected_elems=['[-9, 10]','[-8, 10]','[-7, 10]',
							'[-10, 9]','[-10, 8]',
							'[-9, 7]','[-8, 7]','[-7, 7]',
							'[-6, 6]','[-5, 5]',
							'[-8, 4]','[-7, 4]','[-6, 4]']"""
	def The_choice(self):
		Nvar_num=len(self.List_real_row_elems_count)
		print("\n\n\t\tDo you want default input,random inputs or do you want to input your own selected life cells to begin the game with??")
		try:
			print("\n\n\t\t\tCHOOSE : \n\n\t\t\t\t\"1\" For default input of life cells.\n\t\t\t\t\"2\" For random life cells.\n\t\t\t\t\"3\" For user specified life cell inputs.")
			choice=input("\n\n\t\t\t\t\tEnter your choice : ")
		except ValueError:
			print("\n\n\tError!! Wrong input! Kindly enter the right input!")
			self.The_choice()
		if choice=="1":
			List_selected_elems=['[-9, 10]','[-8, 10]','[-7, 10]',
							'[-10, 9]','[-10, 8]',
							'[-9, 7]','[-8, 7]','[-7, 7]',
							'[-7, 6]','[-7, 5]',
							'[-10, 4]','[-9, 4]','[-8, 4]',
							'[-9, 6]','[-8, 6]','[-7, 4]',
							'[-6, 6]','[-5, 6]',
							'[-9, 8]','[-7, 3]','[-5, 4]',
							'[7, -6]','[7, -5]']
			List_selected_elems.sort()
			print ("\n\n\n\n COORDINATES OF LIFE CELLS SELECTED : ")
			print ("\n\n",List_selected_elems)
			print ("\n\n Number of life cells selected : ",len(List_selected_elems))
			input("\n\n\n\tPress any key to continue... ")
		elif choice=="2":
			List_selected_elems=[]
			temp=[]
			print ("\n\n\t\t\t\t\t\tThe total number of grids are : %d x %d = %d"%(Nvar_num,Nvar_num,Nvar_num**2))
			while (1):
				try:
					gen=int(input("\n\t\t\t\t\t\t\tEnter any number between 10 to %d : "%(Nvar_num**2)))
					while gen<10 or gen>Nvar_num**2:
						print ("\n\n\t\t\tERROR!! You entered the wrong input!! Please try again!!")
						gen=int(input("\n\n\t\t\tEnter any number between 10 to %d : "%(Nvar_num**2)))
					break
				except ValueError:
					print ("\n\n\t\t\tERROR!! You entered the wrong input!! Please try again!!")
			#self.Nvar_init_M
			i=self.Nvar_init_M
			j=self.Nvar_init_N
			k=0
			#print ("\n\n",i,j,k)
			if gen==Nvar_num**2:
				while i!=(-self.Nvar_init_M)+1:
				#while i!=(-self.Nvar_init_M):
					while j!=(-self.Nvar_init_N)-1:
						temp.append(i)
						temp.append(j)
						List_selected_elems.append(str(temp))
						j-=1
						temp=[]
					i+=1
					j=self.Nvar_init_N
					temp=[]
			else:
				while k!=gen:
					x=ran.randint(i,-i)
					y=ran.randint(i,-i)
					temp.append(x)
					temp.append(y)
					try:
						List_selected_elems.index(str(temp))
					except ValueError:
						List_selected_elems.append(str(temp))
						k+=1
					temp=[]
			List_selected_elems.sort()
			print ("\n\n\n\n COORDINATES OF LIFE CELLS SELECTED : ")
			print ("\n\n",List_selected_elems)
			print ("\n\n Number of life cells selected : ",len(List_selected_elems))
			input("\n\n\n\tPress any key to continue... ")
		elif choice=="3":
			temppp=[]
			List_selected_elems=[]
			while (1):
				try:
					print ("\n\n\t\t\t\t\t\tThe total number of grids are : %d x %d = %d"%(Nvar_num,Nvar_num,Nvar_num**2))
					num = int(input("\n\n\t\tEnter any no. of pre-selected cells (less than %d and more than 0!) you want to exist beforehand : "%Nvar_num**2))
					while num<1 or num>Nvar_num**2:
						print ("\n\n\t\t\tERROR! Wrong input! Please enter again!")
						num = int(input("\n\n\t\tEnter any no. of pre-selected cells (less than %d!) you want to exist beforehand : "%Nvar_num**2))
					break
				except ValueError:
					print ("\n\n\t\t\tERROR! Wrong input! Please enter again!")
			print ("\n\n\t\t\t\t\t\tThe range of X coordinates is from  : %d to %d"%(self.Nvar_init_M,-self.Nvar_init_M))
			print ("\n\t\t\t\t\t\tThe range of Y coordinates is from  : %d to %d"%(self.Nvar_init_M,-self.Nvar_init_M))
			for i in range(num):
				if (i+1)%10==1 and (i+1)!=11:
				#if str((i+1))[0]=='1':
					while (1):
						try:
							x_cord = int(input("\nEnter x-axis coordinate for 1st live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							while x_cord<self.Nvar_init_M or x_cord>(-self.Nvar_init_M):
								print ("\n\n\tError!! The value you gave for x coordinate is out of range!! Kindly input again!")
								x_cord = int(input("\nEnter x-axis coordinate for 1st live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							y_cord = int(input("Enter y-axis coordinate for 1st live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							while y_cord>self.Nvar_init_N or y_cord<(-self.Nvar_init_N):
								print ("\n\n\tError!! The value you gave for y coordinate is out of range!! Kindly input again!")
								y_cord = int(input("\nEnter y-axis coordinate for 1st live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							break
						except ValueError:
							print ("\n\n\t\t\tERROR!!! PLEASE ENTER THE RIGHT VALUES!")
					temppp.append(x_cord)
					temppp.append(y_cord)
				elif (i+1)%10==2 and (i+1)!=12:
				#elif str((i+1))[0]=='2':
					while (1):
						try:
							x_cord = int(input("\nEnter x-axis coordinate for 2nd live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							while x_cord<(self.Nvar_init_M) or x_cord>(-self.Nvar_init_M):
								print ("\n\n\tError!! The value you gave for x coordinate is out of range!! Kindly input again!")
								x_cord = int(input("\nEnter x-axis coordinate for 2nd live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							y_cord = int(input("Enter y-axis coordinate for 2nd live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							while y_cord>self.Nvar_init_N or y_cord<(-self.Nvar_init_N):
								print ("\n\n\tError!! The value you gave for y coordinate is out of range!! Kindly input again!")
								y_cord = int(input("\nEnter y-axis coordinate for 2nd live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							break
						except ValueError:
							print ("\n\n\t\t\tERROR!!! PLEASE ENTER THE RIGHT VALUES!")
					temppp.append(x_cord)
					temppp.append(y_cord)
				elif (i+1)%10==3 and (i+1)!=13:
				#elif str((i+1))[0]=='3':
					while (1):
						try:
							x_cord = int(input("\nEnter x-axis coordinate for 3rd live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							while x_cord<self.Nvar_init_M or x_cord>(-self.Nvar_init_M):
								print ("\n\n\tError!! The value you gave for x coordinate is out of range!! Kindly input again!")
								x_cord = int(input("\nEnter x-axis coordinate for 3rd live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							y_cord = int(input("Enter y-axis coordinate for 3rd live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							while y_cord>self.Nvar_init_N or y_cord<(-self.Nvar_init_N):
								print ("\n\n\tError!! The value you gave for y coordinate is out of range!! Kindly input again!")
								y_cord = int(input("\nEnter y-axis coordinate for 3rd live-cell (from %d to %d) : "%(self.Nvar_init_M,-self.Nvar_init_M)))
							break
						except ValueError:
							print ("\n\n\t\t\tERROR!!! PLEASE ENTER THE RIGHT VALUES!")
					temppp.append(x_cord)
					temppp.append(y_cord)
				else:
					while (1):
						try:
							x_cord = int(input("\nEnter x-axis coordinate for %dth live-cell (from %d to %d) : "%(i+1,self.Nvar_init_M,-self.Nvar_init_M)))
							while x_cord<self.Nvar_init_M or x_cord>(-self.Nvar_init_M):
								print ("\n\n\tError!! The value you gave for x coordinate is out of range!! Kindly input again!")
								x_cord = int(input("\nEnter x-axis coordinate for %dth live-cell (from %d to %d) : "%(i+1,self.Nvar_init_M,-self.Nvar_init_M)))
							y_cord = int(input("Enter y-axis coordinate for %dth live-cell (from %d to %d) : "%(i+1,self.Nvar_init_M,-self.Nvar_init_M)))
							while y_cord>self.Nvar_init_N or y_cord<(-self.Nvar_init_N):
								print ("\n\n\tError!! The value you gave for y coordinate is out of range!! Kindly input again!")
								y_cord = int(input("\nEnter y-axis coordinate for %dth live-cell (from %d to %d) : "%(i+1,self.Nvar_init_M,-self.Nvar_init_M)))
							break
						except ValueError:
							print ("\n\n\t\t\tERROR!!! PLEASE ENTER THE RIGHT VALUES!")
					temppp.append(x_cord)
					temppp.append(y_cord)
				List_selected_elems.append(str(temppp))
				temppp=[]
			List_selected_elems.sort()
			print ("\n\n\n\n COORDINATES OF LIFE CELLS SELECTED : ")
			print ("\n\n",List_selected_elems)
			print ("\n\n Number of life cells selected : ",len(List_selected_elems))
			input("\n\n\n\tPress any key to continue... ")
		else:
			print("\n\t\t\t\t\t\tError!! Wrong input! Kindly enter the right input!")
			self.The_choice()
		#print (List_selected_elems)
		#sleep(5)
		k=0
		self.List_all_real=[]
		for i in range(len(self.Dict_VIRTUAL_ROWKEYS_ELEMS)):
			for j in range(len(self.Dict_VIRTUAL_ROWKEYS_ELEMS["r1"])):
				if i==0:
					self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j][str(self.List_virtual_elems[k])]=0
				elif i==(len(self.Dict_VIRTUAL_ROWKEYS_ELEMS)-1):
					self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j][str(self.List_virtual_elems[k])]=0
				else:
					if j==0:
						self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j][str(self.List_virtual_elems[k])]=0
					elif j==(len(self.Dict_VIRTUAL_ROWKEYS_ELEMS['r1'])-1):
						self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j][str(self.List_virtual_elems[k])]=0
					else:
						try:
							temp=list(self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j].keys())[0]
							if -1 < List_selected_elems.index(temp) < len(List_selected_elems):
								self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j][str(self.List_virtual_elems[k])]="\u25A0"
								self.List_all_real.append(self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j])
						except ValueError:
							self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j][str(self.List_virtual_elems[k])]="\u25A1"
							self.List_all_real.append(self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j])

				k+=1
		#pprint (self.Dict_VIRTUAL_ROWKEYS_ELEMS)
		#pprint (self.List_all_real)
		self.List_all=[]
		for i in range(len(self.Dict_VIRTUAL_ROWKEYS_ELEMS)):
			for j in range(len(self.Dict_VIRTUAL_ROWKEYS_ELEMS['r1'])):
				self.List_all.append(self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j])
		#pprint (self.List_all)
		x=0;y=0
		temp_list=[]
		self.List_ULTIMATO_COMBO_ELEMS=[]
		List_ALLL=self.List_all
		NVar_center=self.Nvar_init_N*2+4
		NVar_bottom_right=NVar_center*2
		while y!=(len(self.List_real_column_elems_count)):
			while x!=(len(self.List_real_row_elems_count)):
				for i in range(len(List_ALLL)):
					if i==0:
						temp_list.append(List_ALLL[i])
					if i==1:
						temp_list.append(List_ALLL[i])
					if i==2:
						temp_list.append(List_ALLL[i])
					if i==(NVar_center - 1):
						temp_list.append(List_ALLL[i])
					if i==NVar_center:
						temp_list.append(List_ALLL[i])
					if i==(NVar_center + 1):
						temp_list.append(List_ALLL[i])
					if i==(NVar_bottom_right - 2):
						temp_list.append(List_ALLL[i])
					if i==(NVar_bottom_right - 1):
						temp_list.append(List_ALLL[i])
					if i==NVar_bottom_right:
						temp_list.append(List_ALLL[i])
				x+=1
				self.List_ULTIMATO_COMBO_ELEMS.append(temp_list)
				List_ALLL.pop(0)
				#print (temp_list,"\n\n",len(temp_list))
				temp_list=[]
			List_ALLL.pop(0)
			List_ALLL.pop(0)
			#print ("Broke out of the loop",List_ALLL,"\n")
			x=0
			y+=1
		#pprint (self.List_ULTIMATO_COMBO_ELEMS)
		#self.Birth_and_death_io()
		self.Display_game()
	def Display_game(self):
		sl(0.01)
		if platform=="linux" or platform=="linux2":
			os.system("clear")
		elif platform=="win32":
			os.system('cls')
		#sl(0.1)
		Nvar_num=len(self.List_real_row_elems_count)
		print ("\n\n\tTotal Number of boxes -> (%d x %d) => %d"%(Nvar_num,Nvar_num,Nvar_num**2))
		print ("\n\t           Current game instance => %d"%(self.Nvar_game_instance))
		self.Nvar_game_instance+=1
		print ("\n\n")
		for i in range(len(self.List_ULTIMATO_COMBO_ELEMS)):
			elem=list(self.List_ULTIMATO_COMBO_ELEMS[i][4].values())[0]
			print (elem," ",end="")
			if (i+1)%(len(self.List_real_row_elems_count))==0:
				print ("")
		sl(0.01)
		self.Birth_and_death_io()
		"""
		k=0
		for i in range(len(self.List_virtual_column_elems_count)):
			for j in range(len(self.List_virtual_row_elems_count)):
				elem=self.Dict_VIRTUAL_ROWKEYS_ELEMS[self.List_virtual_rowkeys[i]][j][str(self.List_virtual_elems[k])]
				if elem==0:
					pass
				else:
					print (elem," ",end="")
				k+=1
			print ("")
		"""
	def Birth_and_death_io(self):
		pass
		center_cell=""
		"""List_parallel_COMBO=[]
		for i in range(len(self.List_ULTIMATO_COMBO_ELEMS)):
			l=[]
			for j in range(len(self.List_ULTIMATO_COMBO_ELEMS[i])):
				d={}
				d.update(self.List_ULTIMATO_COMBO_ELEMS[i][j])
				l.append(d)
			List_parallel_COMBO.append(l)"""
		#print ("\n\n")
		#pprint (List_parallel_COMBO)
		List_count_alive_dead=[]
		List_elem_holder=[]
		for i in range(len(self.List_ULTIMATO_COMBO_ELEMS)):
			for j in range(len(self.List_ULTIMATO_COMBO_ELEMS[i])):
				center_cell=list(self.List_ULTIMATO_COMBO_ELEMS[i][4].values())[0]
				#center_cell=list(self.List_ULTIMATO_COMBO_ELEMS[i][4].values())[0]
				key=list(self.List_ULTIMATO_COMBO_ELEMS[i][4].keys())[0]
				#key=list(self.List_ULTIMATO_COMBO_ELEMS[i][4].keys())[0]
				if j==4:
					pass
				else:
					elem=list(self.List_ULTIMATO_COMBO_ELEMS[i][j].values())[0]
					List_count_alive_dead.append(elem)
			if center_cell=='□':
				if List_count_alive_dead.count('■')==3:
					List_elem_holder.append([i,4,key,'■'])
			if center_cell=='■':
				if List_count_alive_dead.count('■')<2:
					List_elem_holder.append([i,4,key,'□'])
				if 1<List_count_alive_dead.count('■')<4:
						pass
				if List_count_alive_dead.count('■')>3:
					List_elem_holder.append([i,4,key,'□'])
			List_count_alive_dead=[]
		l=List_elem_holder
		#print (l)
		for m in range(len(List_elem_holder)):
			self.List_ULTIMATO_COMBO_ELEMS[l[m][0]][l[m][1]][l[m][2]]=l[m][3]
		self.Display_game()


Game_Of_Life()
