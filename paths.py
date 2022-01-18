from os import path

Paths = {}
Paths['Prefix'] = path.join(path.dirname(path.abspath(__file__)), 'assets\\')
Paths['Icon'] = 'mario.png'
Paths['SpriteRImage'] = 'mario_walking/mario6.png'
Paths['SpriteLImage'] = 'firemario_L.png'
Paths['Enemy1Image'] = 'goomba.png'
Paths['Music1'] = 'mario_soundtrack.mp3'
Paths['Projectile'] = 'fireball.png'
Paths['ProjectileSoundEffect'] = 'fireball.mp3'
Paths['ShootingSoundEffect'] = 'fireball.mp3'
Paths['GameOverSoundEffect'] = 'game_over_sound_effect.mp3'
Paths['GameCompleteSoundEffect'] = 'game_complete_sound_effect.mp3'
Paths['Lava'] = 'lava.png'
Paths['DeadPlayer'] = 'ghost.png'
Paths['RestartButton'] = 'restart_btn.png'
Paths['StartButton'] = 'start_btn.png'
Paths['ExitButton'] = 'exit_btn.png'
Paths['Exit'] = 'dirt.png'
Paths['Coin'] = 'coin.png'
Paths['CoinSFX'] = 'coin.wav'
Paths['Background'] = 'bg.png'

for k, v in Paths.items():
    if k != 'Prefix':
        Paths[k] = Paths['Prefix'] + Paths[k]
