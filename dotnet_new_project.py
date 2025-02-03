import sublime
import sublime_plugin
import subprocess
import os

class DotnetNewProjectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        initial_path = "/home/nagyhunor/Documents/nerdstuff/programming"
        
        try:
            target_dir = subprocess.check_output([
                'zenity',
                '--file-selection',
                '--directory',
                '--title=Select Project Location',
                '--filename=' + initial_path + '/'
            ]).decode().strip()
            
            project_name = subprocess.check_output([
                'zenity',
                '--entry',
                '--title=New .NET Project',
                '--text=Enter project name:'
            ]).decode().strip()
            
            if project_name and target_dir:
                project_path = os.path.join(target_dir, project_name)
                
                # Create new dotnet project
                subprocess.run([
                    'dotnet',
                    'new',
                    'console',
                    '-n',
                    project_name,
                    '-o',
                    project_path
                ])
                
                # Create new window and open folder directly
                sublime.run_command('new_window')
                
                def open_project():
                    new_window = sublime.active_window()
                    new_window.set_project_data({'folders': [{'path': project_path}]})
                    
                    # Close the original window
                    self.view.window().run_command('close_window')
                
                sublime.set_timeout(open_project, 300)
                
        except subprocess.CalledProcessError:
            pass
