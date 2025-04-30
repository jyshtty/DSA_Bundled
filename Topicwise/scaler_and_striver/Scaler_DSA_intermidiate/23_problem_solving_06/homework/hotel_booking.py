class Solution:
    def hotel(self, arrive, depart, K):
        dict01 = {}
        guests = 0

        events = [(t, 0) for t in arrive] + [(t, 1) for t in depart]
        events = sorted(events)
        print(events)

        # for i in arrive:
        #     if i not in dict01:
        #         dict01[i] = 1
        #     else:
        #         dict01[i] += 1
        #
        # for i in depart:
        #     if i in dict01:
        #         guests += 1
        #         dict01[i] -= 1
        #
        #     if dict01.get(i) == 0:
        #         del dict01[i]

        for event in events:
            if event[1] == 0:
                guests += 1
            else:
                guests -= 1

            if guests > K:
                return 0
        return 1
        # def hotel(self, A, B, K):
        #     A.sort()
        #     B.sort()
        #     for i in range(len(A)):
        #         if i + K < len(A) and A[i + K] < B[i]:
        #             return 0
        #     return 1



if __name__ == "__main__":
    # A= [41, 10, 12, 30, 0, 17, 38, 36, 45, 2, 33, 36, 39, 25, 22, 5, 41, 24, 12, 33, 19, 30, 25, 12, 36, 8]
    # B= [47, 20, 15, 65, 35, 51, 38, 36, 94, 30, 50, 38, 67, 64, 67, 24, 62, 38, 18, 59, 20, 74, 33, 43, 56, 32]
    A = [1,2,3]
    B = [2,3,4]
    K= 1
    obj = Solution()
    print(obj.hotel(A, B, K))