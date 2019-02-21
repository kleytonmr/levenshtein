import levenshtein as ls 
import pandas as pd 

class Generic:

	def __init__(self, base_a, base_b, sheet_a, sheet_b, nm_a, nm_b, key_a, key_b, extra_a, extra_b): #construct
		self.appended_data = pd.DataFrame()

		# set variable name 
		self.nm_a = nm_a    
		self.nm_b = nm_b
		self.key_a = key_a
		self.key_b = key_b
		self.extra_a = extra_a
		self.extra_b = extra_b

		# import dataset 
		self.read_database(pd.read_excel(pd.ExcelFile(base_a), sheet_a), pd.read_excel(pd.ExcelFile(base_b), sheet_b)) 
	
	@property # getAppend
	def append(self):
		print(self.appended_data.head(100))
		return self.appended_data
	
	@append.setter # setAppend
	def append(self, value):
		self.appended_data = self.appended_data.append(value, ignore_index=True)

	def read_database(self,df1, df2):
		temp = 0
		for i in df1.itertuples():
			for j in df2.itertuples():
				if getattr(i, self.key_a) == getattr(j, self.key_b):
					if getattr(i, self.key_a) != temp:
						key_a = temp = getattr(i, self.key_a)
						key_b = getattr(j, self.key_b)
						self.itaration(key_a, key_b, df1, df2)
						print("Passei aqui {0} {1}" . format(key_a, key_b))
						break
					else:
						break        

	# get the current col and compare the values of the bank "base_a" with the values of the bank "base_b"
	def itaration(self, key_a, key_b, df1, df2): 
		df_temp_a = pd.DataFrame(df1[df1[self.key_a] == key_a])
		df_temp_b = pd.DataFrame(df2[df2[self.key_b] == key_b])
		f= open("log.txt","w+")
		
		for i in df_temp_a.itertuples():
			for j in df_temp_b.itertuples():
				percent = ls.compare(getattr(i, self.nm_a), getattr(j, self.nm_b))
				df = {'index_a':i.Index+2, 'key_a': key_a, 'nm_a':getattr(i,self.nm_a),self.extra_a :getattr(i,self.extra_a), 'index_b':j.Index+2, 'key_b': key_b, 'nm_b':getattr(j,self.nm_b),self.extra_b:getattr(j,self.extra_b), '%': percent}
				self.append = df
				f.write("index:{0}, Nome:{1}, index:{2}, nome:{3} {4}%\n" . format(i.Index+2, getattr(i,self.nm_a), j.Index+2, getattr(j,self.nm_b), percent))
		f.close()
	
	def export(self, file): #export database group by "Semelhança"
		writer = pd.ExcelWriter(file)
		new_df = self.appended_data.loc[self.appended_data.groupby('nm_a', sort=False)['%'].idxmax()]
		new_df.to_excel(writer,'Sheet1')
		writer.save()
	

    


    
    
    
    
    
  