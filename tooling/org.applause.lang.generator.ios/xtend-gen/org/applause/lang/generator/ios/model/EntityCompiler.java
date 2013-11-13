package org.applause.lang.generator.ios.model;

import com.google.common.collect.Iterables;
import com.google.inject.Inject;
import org.applause.lang.applauseDsl.Entity;
import org.applause.lang.generator.ios.ICompilerModule;
import org.applause.lang.generator.ios.model.EntityHeaderFileCompiler;
import org.applause.lang.generator.ios.model.EntityModelExtensions;
import org.applause.lang.generator.ios.model.EntityModuleFileCompiler;
import org.eclipse.emf.common.util.TreeIterator;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.xtext.generator.IFileSystemAccess;
import org.eclipse.xtext.xbase.lib.Extension;
import org.eclipse.xtext.xbase.lib.IterableExtensions;
import org.eclipse.xtext.xbase.lib.IteratorExtensions;
import org.eclipse.xtext.xbase.lib.Procedures.Procedure1;

@SuppressWarnings("all")
public class EntityCompiler implements ICompilerModule {
  @Inject
  @Extension
  private EntityHeaderFileCompiler _entityHeaderFileCompiler;
  
  @Inject
  @Extension
  private EntityModuleFileCompiler _entityModuleFileCompiler;
  
  @Inject
  @Extension
  private EntityModelExtensions _entityModelExtensions;
  
  public void doGenerate(final Resource resource, final IFileSystemAccess fsa) {
    TreeIterator<EObject> _allContents = resource.getAllContents();
    Iterable<EObject> _iterable = IteratorExtensions.<EObject>toIterable(_allContents);
    Iterable<Entity> _filter = Iterables.<Entity>filter(_iterable, Entity.class);
    final Procedure1<Entity> _function = new Procedure1<Entity>() {
      public void apply(final Entity it) {
        String _headerFileName = EntityCompiler.this._entityModelExtensions.headerFileName(it);
        CharSequence _compileHeader = EntityCompiler.this._entityHeaderFileCompiler.compileHeader(it);
        fsa.generateFile(_headerFileName, _compileHeader);
        String _moduleFileName = EntityCompiler.this._entityModelExtensions.moduleFileName(it);
        CharSequence _compileModule = EntityCompiler.this._entityModuleFileCompiler.compileModule(it);
        fsa.generateFile(_moduleFileName, _compileModule);
      }
    };
    IterableExtensions.<Entity>forEach(_filter, _function);
  }
}
