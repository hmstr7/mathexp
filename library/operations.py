
class Calculator:
    def __init__(self, initial:int) -> None:
        self.flow=initial
    def add(self,args: list)->int|Exception:
        try:
            internal_res=self.flow
            for arg in args:
                internal_res+=arg
            self.flow=internal_res
            return internal_res
        except Exception as e:
            return e
    def subtract(self,args: list)->int|Exception:
        try:
            internal_res=self.flow
            for arg in args:
                internal_res-=arg
            self.flow=internal_res
            return internal_res
        except Exception as e:
            return e
    def multiply(self,args: list)->int|Exception:
        try:
            internal_res=self.flow
            for arg in args:
                internal_res=internal_res*arg
            self.flow=internal_res
            return internal_res
        except Exception as e:
            return e
    def divide(self,args: list)->int|Exception:
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
    def power(self,args: list)->int|Exception:
        try:
            internal_res=self.flow
            for arg in args:
                internal_res=internal_res**arg
            self.flow=internal_res
            return internal_res
        except Exception as e:
            return e
    def parse(self,expression:str,depth:int=0)->list|Exception:
        try:
            from library.dictionary import operands
            ignores=1
            exp=list(expression)
            expdict=[] # {id:int,operation:str,arguments:list_int}
            numarray=False
            in_subexpression=False
            subexpression_contents=""
            valid_operands=list(operands.keys())
            curr_operation={"operation":"","arguments":[]}
            curr_numarg=""
            numargs=[]
            for char in exp:
                if not numarray and not in_subexpression:
                    if char in valid_operands:
                        curr_operation["operation"]=char
                        continue
                    elif char=="[":
                        numarray=True
                        continue
                    else:
                        raise Exception("invalid expression")
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
                            numarray=False
                            curr_operation["arguments"]=numargs
                            numargs=[]
                            expdict.append(curr_operation)
                            curr_operation={"operation":"","arguments":[]}
                        elif char==",":
                            try:
                                if "..." in curr_numarg:
                                    sp=curr_numarg.split("...")
                                    numargs.extend(range(int(sp[0]),int(sp[1])))
                                else:
                                    a=int(curr_numarg)
                                    numargs.append(a)
                            except:
                                raise Exception("invalid argument")
                            
                            curr_numarg=""
                        elif char=="(":
                            in_subexpression=True
                            subexpression_contents=""
                        else:
                            curr_numarg+=char
            for operation in expdict:
                getattr(self,operands[operation["operation"]])(args=operation["arguments"])
            return self.flow
        except Exception as e:
            print(e)
            return e


    
    
    
