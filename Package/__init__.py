import sys
import enhance_speach
import getRes
import cleanup

if __name__ == '__main__':
    # enhance_speach.Enhance_speach(sys.argv[1])
    enhance_speach.Enhance_speach(r"F:\code\Audio_classification\dataBase\UrbanSound8K_byclass\person\A2_27.wav")
    # 得到返回值
    result = getRes.main()
    print(result)
    # 清空文件夹
    cleanup.clean()