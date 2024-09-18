team1_num = 5  # количество участников команды 1
score_1 = 34  # счёт команды 1
team1_time = 756  # время выполнения задания командой 1

team2_num = 8  # количество участников команды 2
score_2 = 42  # счёт команды 2
team2_time = 867  # время выполнения задания командой 2

tascs_total = score_1 + score_2  # общее количество решённых задач
time_avg = f'{(756/34 + 867/42)/2:.2f}'  # среднее время решения задачи

ch_rez = ''  # победитель

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    ch_rez = 'победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    ch_rez = 'победа команды Волшебники Данных!'
else:
    ch_rez = 'ничья!'


print('В команде Мастера кода: %s участников' %str(team1_num))
print('В команде Волшебники данных: %s участников' %str(team2_num))
print('Итого сегодня в командах %s и %s участников' %(str(team1_num),str(team2_num)))

print('Команда Мастера кода решила {} задач'.format(str(score_1)))
print('Команда Волшебники данных решила {} задач'.format(str(score_2)))
print(f'Команды решили {str(score_1)} и {str(score_2)} задач')

print('Команда Мастера кода решила задание за {} секунд'.format(str(team1_time)))
print('Команда Волшебники данных решила задание за {} секунд'.format(str(team2_time)))

print(f'Результат битвы: {ch_rez}')
print(f'Сегодня было решено {str(tascs_total)} задач, в среднем по {str(time_avg)} секунд на задачу')
