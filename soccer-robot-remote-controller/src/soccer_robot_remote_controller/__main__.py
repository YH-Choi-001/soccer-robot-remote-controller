from soccer_robot_remote_controller.app import main
from .btconn import BTConn

if __name__ == "__main__":
    btconn = BTConn()
    main(btconn).main_loop()
