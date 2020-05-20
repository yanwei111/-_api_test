import hashlib

class Md5_Hash():
    def hash_md5(self,param):
        hash = hashlib.md5()
        hash.update(param.encode(encoding="utf-8"))
        md5 = hash.hexdigest()
        return md5

if __name__ == "__main__":
    param = "ttt6767"
    md5 = Md5_Hash().hash_md5(param)
    print('md5加密前：',  param)
    print("md5加密后：",  md5)