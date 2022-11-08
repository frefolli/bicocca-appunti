#! /bin/sh

APP_NAME="StaticServer"

# Location of the pid file.
PIDFILE="./server_pid.txt"
COMMAND_LINE="static-server -p 8080"

# Resolve the location of the 'ps' command
PSEXE="/usr/bin/ps"
if [ ! -x "$PSEXE" ]
then
    PSEXE="/bin/ps"
    if [ ! -x "$PSEXE" ]
    then
        echo "Unable to locate 'ps'."
        echo "Please report this message along with the location of the command on your system."
        exit 1
    fi
fi

getpid() {
    if [ -f "$PIDFILE" ]
    then
        if [ -r "$PIDFILE" ]
        then
            pid=`cat "$PIDFILE"`
            if [ "X$pid" != "X" ]
            then
                # It is possible that 'a' process with the pid exists but that it is not the
                #  correct process.  This can happen in a number of cases, but the most
                #  common is during system startup after an unclean shutdown.
                # The ps statement below looks for the specific wrapper command running as
                #  the pid.  If it is not found then the pid file is considered to be stale.
                pidtest=`$PSEXE -p $pid -o args | grep "static-server" | tail -1`
                if [ "X$pidtest" = "X" ]
                then
                    # This is a stale pid file.
                    rm -f "$PIDFILE"
                    echo "Removed stale pid file: $PIDFILE"
                    pid=""
                fi
            fi
        else
            echo "Cannot read $PIDFILE."
            exit 1
        fi
    fi
}

testpid() {
    pid=`$PSEXE -p $pid | grep $pid | grep -v grep | awk '{print $1}' | tail -1`
    if [ "X$pid" = "X" ]
    then
        # Process is gone so remove the pid file.
        rm -f "$PIDFILE"
        pid=""
    fi
}

start() {
    echo "Starting $APP_NAME..."
    getpid
    if [ "X$pid" = "X" ]
    then
        exec nohup $COMMAND_LINE > /dev/null 2>&1 &
        echo $! > $PIDFILE
    else
        echo "$APP_NAME is already running."
        exit 1
    fi
    getpid
    if [ "X$pid" != "X" ]
    then
        echo "Started $APP_NAME."
    else
        echo "Failed to start $APP_NAME."
    fi
}

waitforstop() {
    savepid=$pid
    CNT=0
    TOTCNT=0
    while [ "X$pid" != "X" ]
    do
        # Show a waiting message every 5 seconds.
        if [ "$CNT" -lt "5" ]
        then
            CNT=`expr $CNT + 1`
        else
            echo "Waiting for $APP_NAME to exit..."
            CNT=0
        fi
        TOTCNT=`expr $TOTCNT + 1`

        sleep 1

        testpid
    done

    pid=$savepid
    testpid
    if [ "X$pid" != "X" ]
    then
        echo "Failed to stop $APP_NAME."
        exit 1
    else
        echo "Stopped $APP_NAME."
    fi
}

stopit() {
    echo "Gracefully stopping $APP_NAME..."
    getpid
    if [ "X$pid" = "X" ]
    then
        echo "$APP_NAME was not running."
    else
        kill $pid
        if [ $? -ne 0 ]
        then
            # An explanation for the failure should have been given
            echo "Unable to stop $APP_NAME."
            exit 1
        fi

        waitforstop
    fi
}

case "$1" in

    'start')
        start
        ;;

    'stop')
        stopit
        ;;
    *)
        echo "Usage: $0 { start | stop }"
        exit 1
        ;;
esac

exit 0
