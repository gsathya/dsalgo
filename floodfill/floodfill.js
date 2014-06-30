var lastClicked;
elements = [];
intervalId = 0;

var grid = clickableGrid(10, 10, function(el, row, col, i){
    clear();
    el.className='clicked';

    search({'x': row,
         'y': col});
});

document.body.appendChild(grid);

function clear(){
    elements = [];
    clearInterval(intervalId);

    var selectedElements = document.getElementsByClassName('clicked');
    var i, len = selectedElements.length;
    for(i = 0; i < len; i++)
        selectedElements[0].className = '';
}

function clickableGrid(rows, cols, callback ){
    var i = 0;
    var grid = document.createElement('table');
    grid.className = 'grid';

    for (var r = 0; r < rows; ++r){
        var tr = grid.appendChild(document.createElement('tr'));

        for (var c = 0; c<cols; ++c){
            var cell = tr.appendChild(document.createElement('td'));
            cell.innerHTML = ++i;
            cell.id = i;
            cell.addEventListener('click', (function(el, r, c, i){
                return function(){
                    callback(el, r, c, i);
                }
            })(cell, r, c, i),false);
        }
    }
    return grid;
}

function neighbors(item) {
    var n = [];

    for (var i = -1; i < 2; i++) {
        for (var j = -1; j < 2; j++) {
            n.push({
                'x': i+item['x'],
                'y': j+item['y']
            });
        }
    }

    return n;
}

function search(start){
    var search = document.getElementsByName('search');
    search = search[0].checked? "bfs": "dfs";

    var stack = [start];
    var item;
    var visited = {};

    visited[JSON.stringify(start)] = 1;

    while (stack.length != 0) {
        if (search == "bfs")
            // this is O(n), what madness!
            item = stack.shift();
        else
            item = stack.pop();

        if (item['x'] < 0 || item['x'] > 9)
            continue;

        if (item['y'] < 0 || item['y'] > 9)
            continue;

        var el = document.getElementById(item['x']*10 + item['y'] + 1);
        if (el != undefined) {
            elements.push(el);
        }

        var n = neighbors(item);
        for (var i in n) {
            if (visited[JSON.stringify(n[i])] != 1) {
                visited[JSON.stringify(n[i])] = 1;
                stack.push(n[i]);
            }
        }
    }

    elements.reverse();
    intervalId = window.setInterval(color, 25);
}

function color() {
    if (elements.length == 0){
        clearInterval(intervalId);
        return;
    }

    item = elements.pop();
    item.className = 'clicked';
}
