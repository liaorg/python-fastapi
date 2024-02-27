import hashlib


class StringUtil:
    """
    字符串工具类
    """

    @staticmethod
    def GenerateMd5(data: str) -> str:
        """
        生成MD5
        :param data:
        :return:
        """
        md5_hash = hashlib.md5()
        md5_hash.update(data.encode('utf-8'))
        return md5_hash.hexdigest()
