function letterFrequency(text){

    var hashTable = {}; //O(1)
    var outputList = []; //O(1)

    var cleanString = text.replace(/[^A-Za-z]+/g, '').toLowerCase() //O(3)

    for (eachLetter of cleanString){ //O(n)
      (!(hashTable.hasOwnProperty(eachLetter))) ? hashTable[eachLetter] = 1 : hashTable[eachLetter] ++
      }

    for (key in hashTable){ //O(n)
      var pair = []
      pair.push(key);
      pair.push(parseInt(hashTable[key]))
      outputList.push(pair) //O(2)
    }

    console.log(outputList)
    var arr = outputList.sort(function(a,b) {
      if (a[1] === b[1]){
        return (a > b) ? 1 : -1;
      }
      return b[1] - a[1]
      });
    console.log(arr);
  };
letterFrequency("As long as I'm learning something, I figure I'm OK - it's a decent day.")
