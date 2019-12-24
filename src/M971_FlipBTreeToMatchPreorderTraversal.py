count = [0]


def func(root, i, voyage):
    # i=i-1
    # global count
    if root.val == voyage[i - 1]:
        if root.right and root.left:
            if root.right.val == voyage[((2 * i) + 1) - 1] and root.left.val == voyage[(2 * i) - 1]:
                func(root.left, 2 * i, voyage)
                func(root.right(2 * i) + 1, voyage)
            else:
                if root.left.val == voyage[((2 * i) + 1) - 1] and root.right.val == voyage[(2 * i) - 1]:
                    count[0] += 1
                    func(root.right, 2 * i, voyage)
                    func(root.left(2 * i) + 1, voyage)
                else:
                    print(root.right.val, voyage[(2 * i) + 1])
                    print(root.left.val, voyage[2 * i])
                    count[0] = -1
                    print("Unable to exchange")
                    print(count)
                    return
    else:
        print(root.val, voyage[i])
        count[0] = -1
        print(count)
        return

        # voyage=[0]+voyage


func(root, 1, voyage)
# print(count)
if count[0] == 0:
    return []
else:
    return count