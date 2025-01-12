
class Calculator:
    '''
    # Calculator class
    ## Inputs:
    - initial: int - initial value of calculator's flow
    ## Methods
    - parse(expression: str) - executes given expression string (this changes calculator's flow, obviously)
    - reset() - sets the flow back to initial.
    - set(value: int|float) - sets the flow to the value provided.
    '''
    def __init__(self, initial:int) -> None:
        self.flow=initial
        self.initial_value=initial

    ## Private methods ##
    # If you want to make a new operand, put it's function here, and refer to the it by the method's name (without __) in mathexp/dictionary.py   
    def __add(self,args: list):
        try:
            internal_res=self.flow
            for arg in args:
                internal_res+=arg
            self.flow=internal_res
            return internal_res
        except Exception as e:
            return e
    def __subtract(self,args: list):
        try:
            internal_res=self.flow
            for arg in args:
                internal_res-=arg
            self.flow=internal_res
            return internal_res
        except Exception as e:
            return e
    def __multiply(self,args: list):
        try:
            internal_res=self.flow
            for arg in args:
                internal_res=internal_res*arg
            self.flow=internal_res
            return internal_res
        except Exception as e:
            return e
    def __divide(self,args: list):
        try:
            internal_res=self.flow
            for arg in args:
                if arg==0:
                    raise Exception("Cannot divide by zero")
                internal_res=internal_res/arg
            self.flow=internal_res
            return internal_res
        except Exception as e:
            return e
    def __power(self,args: list):
        try:
            internal_res=self.flow
            for arg in args:
                internal_res=internal_res**arg
            self.flow=internal_res
            return internal_res
        except Exception as e:
            return e
    def __mean(self,args: list):
        import mathexp.custom.statistics1 as st1
        try:
            self.flow=st1.mean(args)
            return st1.mean(args)
        except Exception as e:
            return e
    def __median(self,args: list):
        import mathexp.custom.statistics1 as st1
        try:
            self.flow=st1.median(args)
            return st1.median(args)
        except Exception as e:
            return e
    def __range(self,args: list):
        import mathexp.custom.statistics1 as st1
        try:
            self.flow=st1.range_s(args)
            return st1.range_s(args)
        except Exception as e:
            return e
           
        
    #######################

    ## Public methods ##
    def parse(self,expression:str)->list|Exception:
        try:
            from mathexp.dictionary import operands
            ignores=1
            exp=list(expression)
            expdict=[] 
            numarray=False
            in_subexpression=False
            in_special=False
            subexpression_contents=""
            valid_operands=list(operands.keys())
            curr_operation={"operation":"","arguments":[]}
            curr_numarg=""
            curr_operand=""
            numargs=[]
            for char in exp:
                if not numarray and not in_subexpression:
                    if char=="[":
                        if curr_operand in valid_operands:
                            numarray=True
                            curr_operation["operation"]=curr_operand
                            curr_operand=""
                        else:
                            curr_operand=""
                            raise Exception("invalid operand: "+curr_operand)
                    else:
                        curr_operand+=char
                else:
                    if in_subexpression:
                        if char==")":
                            ignores-=1
                            if ignores<1:
                                try:
                                    in_subexpression=False
                                    calc_local=Calculator(0)
                                    calc_local.parse(subexpression_contents)
                                    curr_numarg=str(calc_local.flow)
                                except Exception as e:
                                    raise Exception("Failed to parse subexpression: "+str(e))
                            else:
                                subexpression_contents+=char
                        elif char=="(":
                            ignores+=1
                            subexpression_contents+=char
                        else:
                            subexpression_contents+=char
                    else:
                        if char=="]":
                            if curr_numarg!="":
                                try:
                                    if curr_numarg[0]=="_":
                                        if "<" in curr_numarg:
                                            try:
                                                import mathexp.special
                                                curr_numarg=curr_numarg[1:]
                                                func_n_args=curr_numarg.split("<")
                                                try:
                                                    func_name=mathexp.special.special_alias[func_n_args[0]]
                                                    func=getattr(mathexp.special,func_name)
                                                except:
                                                    try:
                                                        func=getattr(mathexp.special,func_n_args[0])
                                                    except:
                                                        raise Exception("Invalid argument: incorrect special")
                                                numargs.append(func(func_n_args[1]))
                                            except:
                                                raise Exception("Invalid argument: incorrect special")
                                    elif "..." in curr_numarg:
                                        sp=curr_numarg.split("...")
                                        numargs.extend(range(int(sp[0]),int(sp[1])))
                                    else:
                                        try:
                                            a=int(curr_numarg)
                                            numargs.append(a)
                                        except:
                                            try: 
                                                a=float(curr_numarg)
                                                numargs.append(a)
                                            except:
                                                raise Exception("invalid argument: "+curr_numarg)
                                except:
                                    raise Exception("invalid argument: "+curr_numarg)
                            
                            numarray=False
                            curr_operation["arguments"]=numargs
                            numargs=[]
                            expdict.append(curr_operation)
                            curr_operation={"operation":"","arguments":[]}
                            curr_numarg=""
                        elif char==",":
                            try:
                                if curr_numarg[0]=="_":
                                    if "<" in curr_numarg:
                                        try:
                                            import mathexp.special
                                            curr_numarg=curr_numarg[1:]
                                            func_n_args=curr_numarg.split("<")
                                            try:
                                                func_name=mathexp.special.special_alias[func_n_args[0]]
                                                func=getattr(mathexp.special,func_name)
                                            except:
                                                try:
                                                    func=getattr(mathexp.special,func_n_args[0])
                                                except:
                                                    raise Exception("Invalid argument: incorrect special")
                                            numargs.append(func(func_n_args[1]))
                                        except:
                                            raise Exception("Invalid argument: incorrect special")
                                elif "..." in curr_numarg:
                                    sp=curr_numarg.split("...")
                                    numargs.extend(range(int(sp[0]),int(sp[1])))
                                else:
                                    try:
                                        a=int(curr_numarg)
                                        numargs.append(a)
                                    except:
                                        try: 
                                            a=float(curr_numarg)
                                            numargs.append(a)
                                        except:
                                            raise Exception("invalid argument: "+curr_numarg)
                            except:
                                raise Exception("invalid argument: "+curr_numarg)
                            
                            curr_numarg=""
                        elif char=="(":
                            in_subexpression=True
                            subexpression_contents=""
                        else:
                            curr_numarg+=char
            for operation in expdict:
                out=getattr(self,"_Calculator__"+operands[operation["operation"]])(args=operation["arguments"])
                if type(out)==Exception:
                    raise out
            return self.flow
        except Exception as e:
            print(e)
            return e
    def reset(self):
        self.flow=self.initial_value
    def set(self,value:int|float):
        self.flow=value

    
    
    
