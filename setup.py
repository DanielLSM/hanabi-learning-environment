from skbuild import setup

setup(name='hanabi_learning_environment',
      version='0.0.1',
      description='Learning environment for the game of hanabi.',
      author='deepmind/hanabi-learning-environment',
      packages=[
          'hanabi_learning_environment', 'hanabi_learning_environment.agents',
          'hanabi_learning_environment.agents.rainbow',
          'hanabi_learning_environment.agents.rainbow.third_party',
          'hanabi_learning_environment.agents.rainbow.third_party.dopamine'
      ],
      install_requires=['cffi'])
