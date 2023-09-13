---
layout: page
icon: fas fa-tasks
order: 1
type: hacks
---

<link rel="stylesheet" href="{{site.baseurl}}/assets/css/todo.css" />
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
<script type="text/javascript" language="javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
<script src="{{site.baseurl}}/assets/js/pages/todo.js"></script>
<body onload="getNewQuote();">
<div id = "quoteDiv" class = "background">
    <p id="quote" class="quote"></p>
    <p id="author" class="author"></p>
</div>

<br>

<div class="table-wrapper background">
    <table id="TODO" class="todo-table">
        <thead>
            <th>Index</th>
            <th>Task name</th>
            <th>Class Name</th>
            <th>Deadline</th>
            <th>Done</th>
        </thead>
        <tbody>
        </tbody>
    </table>
</div>



<script>
    var table1 = document.getElementById("TODO").getElementsByTagName('tbody')[0];
    var indexCount = localStorage.getItem("indexCount");
    readStorage();
    let table = new DataTable('#TODO');
    table.draw();
</script>
</body>