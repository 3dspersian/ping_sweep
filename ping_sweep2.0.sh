for i in {1..254}; do (ping -c 1 XX.XX.XX.$i | grep 'bytes from' &); done
