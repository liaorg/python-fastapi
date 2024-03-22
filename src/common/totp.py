import base64
import hashlib
import hmac
import struct
import time

"""
# 示例用法：
s = bytes('你的密钥', 'utf-8')
key = base64.b32encode(s)
current_hotp = hotp(key)  # 获取当前 HOTP
print("Current HOTP:", key, current_hotp)

current_totp = totp(key)  # 获取当前 TOTP
print("Current TOTP:", key, current_totp)
"""


def hotp(secret, step=30, digits=6):
    """
    实现 HOTP 算法
    :param secret: 秘钥，一个唯一的、随机生成的字符串
    :param step: 步长，默认是 1
    :param digits: OTP 的位数。默认是 6 位
    :return: 当前 step 的 OTP
    """
    key = base64.b32decode(secret, True)
    step = int(step)  # 计算当前步长

    # 创建一个字节串，包含时间戳和秘钥，并对它进行哈希处理
    hasher = hmac.new(key, struct.pack(">Q", step), hashlib.sha1)
    hmac_result = hasher.digest()

    # 获取哈希结果的最后一个字节，并转换为整数
    offset = int(hmac_result[-1] & 0xF)

    # 从哈希结果中获取 4 个字节，用于计算 OTP
    binary_otp = struct.unpack(">I", hmac_result[offset : offset + 4])[0]
    otp = binary_otp & 0x7FFFFFFF
    otp = otp % (10**digits)

    # 格式化 OTP，确保它总是有指定的位数
    return f"{otp:0{digits}d}"


def totp(secret, time_step=30, time_digits=6):
    """
    实现 TOTP 算法，基于 HOTP 算法
    :param secret: 秘钥，一个唯一的、随机生成的字符串
    :param time_step: 时间步长，以秒为单位。默认是 30 秒
    :param time_digits: OTP 的位数。默认是 6 位
    :return: 当前时间步的 OTP
    """
    # 计算当前时间步长
    timestamp = int(time.time() / time_step)
    return hotp(secret, step=timestamp, digits=time_digits)
