let account;
const childacount = "0x49c0B675f0eA9491cd6ef3f1597Ce38eEF9cb720";
const onenft = 1 ;
let Tokennumber = 0;  //토큰 번호(NFT 구별)

//로컬FS에서 JSON의 CID 얻어오기
let jscd = null;
let xmlhttp = new XMLHttpRequest();
xmlhttp.open("GET", "/static/data/CID.txt", false);
xmlhttp.send();
//파일 로드 성공 시 파일에서 읽은 텍스트를 jscd에 담음
if (xmlhttp.status == 200) { 
  jscd = xmlhttp.responseText;
}
jscd = "ipfs://"+jscd+"/"
//alert(jscd) //테스트용



//kaikas 지갑 연결
async function connect() {
  const accounts = await klaytn.enable();
  if (klaytn.networkVersion === 8217) {
    console.log("메인넷");
  } else if (klaytn.networkVersion === 1001) {
    console.log("테스트넷");
  } else {
    alert("ERROR: 클레이튼 네트워크로 연결되지 않았습니다!");
    return;
  }
  account = accounts[0];
  caver.klay.getBalance(account).then(function (balance) {
    document.getElementById("myWallet").innerHTML = `지갑주소: ${account}`;
    document.getElementById("myKlay").innerHTML = `잔액: ${caver.utils.fromPeb(
      balance,
      "KLAY"
    )} KLAY`;
  });

}

async function setBaseURI() {
  const myContract = new caver.klay.Contract(ABI, CONTRACTADDRESS);
  await myContract.methods.setBaseURI(jscd).send({
    from: account,
    gas: 6000000,
  });
}



async function airDropMint() {
  const myContract = new caver.klay.Contract(ABI, CONTRACTADDRESS);
  await myContract.methods.airDropMint(childacount, onenft).send({
    from: account,
    gas: 6000000,
  });
}

async function totalSupply(){
  const myContract = new caver.klay.Contract(ABI, CONTRACTADDRESS);
  ret = await myContract.methods.totalSupply().call();
  Tokennumber = Number(ret)+1;
  document.getElementById("tokenNubmer").innerHTML = "현재 토큰:"+ Tokennumber;
}
