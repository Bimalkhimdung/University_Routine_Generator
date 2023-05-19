
def selection(score_lst, routine_lst):
    for i in range(len(score_lst)):
        for j in range(i + 1, len(score_lst)):

            if score_lst[i] < score_lst[j]:
                score_lst[i], score_lst[j] = score_lst[j], score_lst[i]
                routine_lst[i], routine_lst[j] = routine_lst[j], routine_lst[i]
                

    return routine_lst, score_lst