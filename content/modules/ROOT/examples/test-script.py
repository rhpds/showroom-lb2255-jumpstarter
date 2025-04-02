from jumpstarter.common.utils import env
import sys

with env() as dut:  # use the jumpstarter shell session
    dut.power.off()
    dut.flasher.flash("simple.qcow2")
    dut.power.on()

    with dut.console.pexpect() as p:
        p.logfile = sys.stdout.buffer  # forward console output to stdout
        # login into the dut
        p.expect_exact("dut login:", timeout=600)
        p.sendline("jumpstarter")
        p.expect_exact("Password:")
        p.sendline("password")
        # wait for the shell prompt
        p.expect_exact("[jumpstarter@dut ~]$")
        # execute test commands
        p.sendline("echo hello from dut")
        p.expect_exact("[jumpstarter@dut ~]$")

    dut.power.off()
