from module_name.utils.base_util import BaseUtil 

if __name__ == "__main__":
    try:
        encodestr = BaseUtil.encode("test")
        print(encodestr)
        decodestr = BaseUtil.decode(encodestr)
        print(decodestr)
    except Exception as err:
        print(f"{err}")