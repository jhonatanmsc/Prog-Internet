//exercicio 01
var firstName = 'joao';
var interest = 'lol';
var hobby = 'asdasdf';

function concatenar(firstName, interest, hobby){
	let awesomeMessage = 'Hi, my name is ' + firstName + '. I love ' + interest + '. In my spare time, I like to ' + hobby + '.';
	return awesomeMessage;
}

console.log( concatenar(firstName, interest, hobby) );


//exercicio 02
var listMusic = [];

function tamanhoLista(listMusic){
	let tam = listMusic.length;
	let phrase = '';

	if(tam > 4){
		phrase = "this is a large group";
	}else if(tam == 4){
		phrase = "quartet";
	}else if(tam == 3){
		phrase = "trio";
	}else if(tam == 2){
		phrase = "duet";
	}else if(tam == 1){
		phrase = "solo";
	}else if(tam == 0){
		phrase = "not a group";
	}

	return phrase;
}

tamanhoLista(listMusic);


//exercicio 03
function mostrarAssentos(){
	for (var i = 0; i < 26; i++) {
		for (var j = 0; j < 100; j++) {
			console.log( i + '-' + j );
		}
	}
}
mostrarAssentos();


//exercicio 04
function fizzBuzz(){
	for (var i = 1; i <= 100; i++) {
		if(i % 3 && i % 5){
			console.log("FizzBuzz");
		}else if(i % 3){
			console.log("Fizz");
		}else if(i % 5){
			console.log("Buzz");
		}else{
			console.log(i);
		}
	}
}
fizzBuzz();


//exercicio 05
var num = 3;
function laugh(num){
	let phrase = '';
	for (var i = 1; i <= num; i++) {
		phrase += 'ha';
	}
	phrase += '!';
	console.log(phrase);
}


//exercicio 06
var numbers = [
	[ 243, 12, 23, 12, 45, 45, 78, 66, 223, 3 ],
	[ 34, 2, 1, 553, 23, 4, 66, 23, 4, 55 ],
	[ 67, 56, 45, 553, 44, 55, 5, 428, 452, 3 ],
	[ 12, 31, 55, 445, 79, 44, 674, 224, 4, 21 ],
	[ 4, 2, 3, 52, 13, 51, 44, 1, 67, 5 ],
	[ 5, 65, 4, 5, 5, 6, 5, 43, 23, 4424 ],
	[ 74, 532, 6, 7, 35, 17, 89, 43, 43, 66 ],
	[ 53, 6, 89, 10, 23, 52, 111, 44, 109, 80 ],
	[ 67, 6, 53, 537, 2, 168, 16, 2, 1, 8 ],
	[ 76, 7, 9, 6, 3, 73, 77, 100, 56, 100 ]
];

function parImpar(numbers){
	for (var i = 0; i < numbers.length; i++) {
		for (var j = 0; j <= numbers.length; j++) {
			if (numbers[i][j] % 2 == 0){
				numbers[i][j] = 'even';
			}
			else{
				numbers[i][j] = 'odd';

			}
		}
	}

}
parImpar(numbers);


//exercicio 07
var savingsAccount = {
	balance: 1000,
	interestRatePercent: 1,
	deposit: function addMoney(amount) {
		if (amount > 0) {
			savingsAccount.balance += amount;
		}
	},
	withdraw: function removeMoney(amount) {
		var verifyBalance = savingsAccount.balance - amount;
		if (amount > 0 && verifyBalance >= 0) {
			savingsAccount.balance -= amount;
		}
	},
	printAccountSummary: function AccountSummary(){
		console.log('Welcome!');
		console.log('Your balance is currently ' + this.balance + ' and your interest rate is ' + this.interestRatePercent + '%.');
	}
};