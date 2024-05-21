import configparser
from sumolib import checkBinary
import os
import sys

def import_train_configuration(config_file):
    content = configparser.ConfigParser()
    content.read(config_file)
    config = {
        'gui': content['simulation'].getboolean('gui'),
        'total_episodes': content['simulation'].getint('total_episodes'),
        'max_steps': content['simulation'].getint('max_steps'),
        'n_cars_generated': content['simulation'].getint('n_cars_generated'),
        'green_duration': content['simulation'].getint('green_duration'),
        'yellow_duration': content['simulation'].getint('yellow_duration'),
        'num_layers': content['model'].getint('num_layers'),
        'width_layers': content['model'].getint('width_layers'),
        'batch_size': content['model'].getint('batch_size'),
        'learning_rate': content['model'].getfloat('learning_rate'),
        'training_epochs': content['model'].getint('training_epochs'),
        'memory_size_min': content['memory'].getint('memory_size_min'),
        'memory_size_max': content['memory'].getint('memory_size_max'),
        'num_states': content['agent'].getint('num_states'),
        'num_actions': content['agent'].getint('num_actions'),
        'gamma': content['agent'].getfloat('gamma'),
        'models_path_name': content['dir']['models_path_name'],
        'sumocfg_file_name': content['dir']['sumocfg_file_name']
    }
    return config

def import_test_configuration(config_file):
    content = configparser.ConfigParser()
    content.read(config_file)
    config = {
        'gui': content['simulation'].getboolean('gui'),
        'max_steps': content['simulation'].getint('max_steps'),
        'n_cars_generated': content['simulation'].getint('n_cars_generated'),
        'episode_seed': content['simulation'].getint('episode_seed'),
        'green_duration': content['simulation'].getint('green_duration'),
        'yellow_duration': content['simulation'].getint('yellow_duration'),
        'num_states': content['agent'].getint('num_states'),
        'num_actions': content['agent'].getint('num_actions'),
        'sumocfg_file_name': content['dir']['sumocfg_file_name'],
        'models_path_name': content['dir']['models_path_name'],
        'model_to_test': content['dir'].getint('model_to_test')
    }
    return config

def set_sumo(gui, sumocfg_file_name, max_steps):
    if 'SUMO_HOME' in os.environ:
        tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
        sys.path.append(tools)
    else:
        sys.exit("please declare environment variable 'SUMO_HOME'")
    sumoBinary = checkBinary('sumo-gui' if gui else 'sumo')
    return [sumoBinary, "-c", os.path.join('sumo_files', sumocfg_file_name), "--no-step-log", "true", "--waiting-time-memory", str(max_steps)]

def set_train_path(models_path_name):
    models_path = os.path.join(os.getcwd(), models_path_name)
    os.makedirs(models_path, exist_ok=True)
    dir_content = os.listdir(models_path)
    previous_versions = [int(name.split("_")[1]) for name in dir_content if name.startswith('model_')] or [0]
    new_version = str(max(previous_versions) + 1)
    data_path = os.path.join(models_path, f'model_{new_version}')
    os.makedirs(data_path, exist_ok=True)
    return data_path

def set_test_path(models_path_name, model_n):
    model_folder_path = os.path.join(os.getcwd(), models_path_name, f'model_{model_n}')
    if not os.path.isdir(model_folder_path):
        sys.exit(f'The model number specified does not exist in the models folder: model_{model_n}')
    plot_path = os.path.join(model_folder_path, 'test')
    os.makedirs(plot_path, exist_ok=True)
    return model_folder_path, plot_path
