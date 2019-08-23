"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""

        self.ram = [0] * 256
        self.pc = 0 # [] ?
        self.registers = [0] * 8
        self.ir = []
        self.mdr = []
        self.mar = []
        self.fl = []
        self.PRN = 0b01000111
        self.ADD = 0b10100000
        self.SUB = 0b10100001
        self.MUL = 0b10100010
        self.LDI = 0b10000010
        self.HLT = 0b00000001
        self.DIV = 0b10100011
        self.MOD = 0b10100100


    def PRN_OP(self):
        pass
    def LDI_OP(self):
        pass
    def HLT_OP(self):
        pass
    def MUL_OP(self, reg_a, reg_b):
        pc = self.pc
        self.registers[reg_a] *= self.registers[reg_b]
        pc +=1
    def ADD_OP(self, reg_a, reg_b):
        pc = self.pc
        self.registers[reg_a] += self.registers[reg_b]
        pc += 1
    def SUB_OP(self, reg_a, reg_b):
        pc = self.pc
        self.registers[reg_a] -= self.registers[reg_b]
        pc += 1
    def DIV_OP(self, reg_a, reg_b):
        pc = self.pc
        self.registers[reg_a] /= self.registers[reg_b]
        pc += 1
    def MOD_OP(self, reg_a, reg_b):
        pc = self.pc
        self.registers[reg_a] %= self.registers[reg_b]
        pc += 1
    def ram_read(self, mem_addr):
        return self.ram[mem_addr]

    def ram_write(self, mem_addr, value):
        self.ram[mem_addr] = value

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        ADD, MUL, SUB, DIV, MOD = (self.ADD, self.MUL, self.SUB, self.DIV, self.MOD)
        ADD_OP, MUL_OP = (self.ADD_OP, self.MUL_OP)
        SUB_OP, DIV_OP, MOD_OP = (self.SUB_OP, self.DIV_OP, self.MOD_OP)
        pc = self.pc
        if op is ADD:
            ADD_OP(reg_a, reg_b)
            pc += 1
        elif op is MUL:
            MUL_OP(reg_a, reg_b)
            pc += 1
        elif op is SUB:
            SUB_OP(reg_a, reg_b)
            pc += 1
        elif op is DIV:
            DIV_OP(reg_a, reg_b)
            pc += 1
        elif op is MOD:
            MOD_OP(reg_a, reg_b)
            pc += 1
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """
        print(f"TRACE: %02X | %02X %02X %02X |" % (
        self.pc,
        # self.fl,
        # self.ie,
        self.ram_read(self.pc),
        self.ram_read(self.pc + 1),
        self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.registers[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pc = self.pc
        ram = self.ram
        ram_length = len(ram)
        i = 0
        running = True
        command = ram[pc]
        while True:
            pass
