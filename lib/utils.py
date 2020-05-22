
class Utils():
    def set_res_data(self,res):
        if res:
            return res.lower().replace('"":""','=').replace('"":""','=')

if __name__ == "__main__":
    Utils().set_res_data({"username":"lsxd","password":"123456","isRemember":0})