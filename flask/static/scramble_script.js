    var phrases = ["Sai Vegasena","Programmer","Security Researcher", "Machine Learning Enthusiast"];
    var scramble = new TextScramble(document.getElementById("name"));
    var count = 0;
    var tick = function tick() {
      scramble.setText(phrases[count]).then(function () {
        setTimeout(tick, 1700);
      });
      count = (count + 1) % phrases.length;
    };
    tick();
