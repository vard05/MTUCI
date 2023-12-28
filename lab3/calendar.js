var days = [
    'Воскресенье',
    'Понедельник',
    'Вторник',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота'
];

var d = new Date();
var n = d.getDay();
var month = d.getMonth()
var day = d.getDate()

month += 1

document.getElementById('dow').innerHTML = days[n]
document.getElementById('fd').innerHTML = `${day}.${('0' + month).slice(-2)}`