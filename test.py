from pipe_viper.pipe_viper import run_pwsh, run_pwsh_cmd


p_var = run_pwsh(".\\pwsh\\Get-EnvPath.ps1")

print(p_var)

