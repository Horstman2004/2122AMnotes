var game = new Phaser.Game(800,600,Phaser.AUTO,'my-game',{
  preload: preload,
  create: create,
  update: update
});

//global variables
var logo;
var spacebar;

//required functions
function preload(){
  game.load.image('phaser-logo','assets/phaser.png');
}

function create(){
  logo = game.add.image(400,300,'phaser-logo');
  logo.anchor.setTo(0.5,0.5);
  spacebar = game.input.keyboard.addKey(Phaser.KeyCode.SPACEBAR);
}

//This Runs Every Single Frame
function update(){
  if (spacebar.justDown) {
    game.stage.backgroundColor = Phaser.Color.getRandomColor();
  }
}


//custom functions