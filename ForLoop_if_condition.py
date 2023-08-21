class ABC:
    def collect_data_warn_start_stop(self,
        esa_warning_active,
    ):

        start_idx = int(0.1 / 0.01)
        #esa_warning_active=[0,0,0,0,0,0,0,0,0,0,1]
        for idx, val in enumerate(esa_warning_active[start_idx:]):
            if val == 1:
                idx += start_idx
                if esa_warning_active[idx - 1] == 0:
                    print("success")

obj=ABC()   
obj.collect_data_warn_start_stop([0,0,0,0,0,0,0,0,0,0,1]) 
