class Addition:

    @staticmethod
    def addition(num1, num2):
        """
        :param num1: string
        :param num2: string
        :return: string
        """
        result = []

        num_max, num_min = list(num1), list(num2)

        if len(num_max) < len(num_min):
            num_max, num_min = list(num2), list(num1)

        len_max, len_min = len(num_max), len(num_min)

        # 进位
        temp = 0
        for i in range(len_max):
            try:
                a = num_max.pop()
            except IndexError:
                a = 0
            try:
                b = num_min.pop()
            except IndexError:
                b = 0
            res = temp + int(a) + int(b)
            if res > 9:
                res = res - 10
                temp = 1
            else:
                temp = 0
            result.insert(0, str(res))

        return ''.join(result)


if __name__ == '__main__':
    print(Addition.addition('1111211111111111111111111111111111111111111119', '111'))
