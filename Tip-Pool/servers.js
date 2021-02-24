let serverNameInput = document.getElementById('serverName');
let serverForm = document.getElementById('serverForm');

let serverTbody = document.querySelector('#serverTable tbody');

let allServers = {};
let serverId = 0;

serverForm.addEventListener('submit', submitServerInfo);

// create server object and add to allServers, update html and reset input
function submitServerInfo(evt) {
  if (evt) evt.preventDefault(); // when running tests there is no event

  let serverName = serverNameInput.value;

  if (serverName !== '') {
    serverId++;
    allServers['server' + serverId] = { serverName };

    updateServerTable();

    serverNameInput.value = '';
  }
}

function appendDeleteBtn(tr, type) {
  let newTd = document.createElement('td');
  newTd.className = 'deleteBtn';
  newTd.innerText = 'X';

  newTd.addEventListener('click', removeEle);

  tr.append(newTd);
}

function removeEle(evt) {
  let ele = evt.target.closest('tr');

  delete allServers[ele.id];

  ele.parentNode.removeChild(ele);
  updateServerTable();
}

// Create table row element and pass to appendTd function with input value
function updateServerTable() {
  serverTbody.innerHTML = '';

  for (let key in allServers) {
    let curServer = allServers[key];

    let newTr = document.createElement('tr');
    newTr.setAttribute('id', key);

    let tipAverage = sumPaymentTotal('tipAmt') / Object.keys(allServers).length;

    // let deleteBtn = document.createElement('td')
    // deleteBtn.innerText = 'X'

    appendTd(newTr, curServer.serverName);
    appendTd(newTr, '$' + tipAverage.toFixed(2));
    appendDeleteBtn(newTr, 'server');


    serverTbody.append(newTr);
  }
}
